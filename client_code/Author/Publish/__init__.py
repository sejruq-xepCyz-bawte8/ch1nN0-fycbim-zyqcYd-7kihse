from ._anvil_designer import PublishTemplate
from anvil import *
import anvil.server
from anvil_extras import Autocomplete, Slider
from ...Cheteme.Memory import genres, keywords, awesome
from ...Cheteme.Author.DetectType import parse_type
from ...Cheteme.Author.ParseUri import parse_uri
from anvil.js.window import jQuery as jQ
from ...Cheteme.ElementsHtml import cover_non_cached
from ...Cheteme.Contrast import adjust_color_for_contrast
import anvil.image
import base64

class Publish(PublishTemplate):
  def __init__(self, data: dict = None, **properties):
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.data = self.check_data(data)
    self.cover = self.dom_nodes['cover']
    self.update_cover()
    self.init_components(**properties)

    #inputs
    self.input = ColumnPanel()
    self.title = TextBox(placeholder = 'заглавие')
    self.title.add_event_handler('change', self.input_change)
    self.input.add_component(self.title)
    
    self.type = DropDown(placeholder = 'тип', include_placeholder=True)
    self.type.add_event_handler('change', self.input_change)
    self.auto_type()
    self.type.items = self.data['types']
    self.type.selected_value = self.data['type']
    self.input.add_component(self.type)

    self.genre = DropDown(placeholder = 'жанр', include_placeholder=True)
    self.genre.items = genres.genre_names_in_level(2)
    self.genre.add_event_handler('change', self.input_change)
    self.input.add_component(self.genre)

    self.subgenre = DropDown(placeholder = 'под-жанр', include_placeholder=True)
    self.subgenre.add_event_handler('change', self.input_change)
    self.input.add_component(self.subgenre)

    self.keywords = Autocomplete.Autocomplete(placeholder = 'ключови думи', include_placeholder=True)
    self.keywords.suggestions = keywords.get_column('bg')
    self.keywords.add_event_handler('suggestion_clicked', self.input_change)
    self.input.add_component(self.keywords)

    self.keywords_label = Link(icon='fa:tags')
    self.keywords_label.icon_align = 'right'
    self.keywords_label.add_event_handler('click', self.input_change)
    self.input.add_component(self.keywords_label)

    #design inputs
    self.cover_file = FileLoader(text = "корица", border = 'unset', icon = 'fa:image')
    self.cover_file.id = 'cover'
    self.cover_file.add_event_handler('change', self.new_cover)
    self.add_component(self.cover_file, slot = 'design')

    self.font = DropDown(placeholder = 'шрифт', include_placeholder=True)
    self.font.id = 'font'
    self.font.items = ['serif', 'monospace', 'Great Vibes', 'Alumni Sans', 'Noto Sans Display']
    self.font.add_event_handler('change', self.design_change)
    self.add_component(self.font, slot = 'design')


    #results
    self.results = ColumnPanel()
    self.uri = Label()
    self.results.add_component(self.uri)
    

    # ading panels
    self.add_component(self.input)
    self.add_component(self.results)

    self.publush = Button(text = 'Публикувай')
    self.publush.add_event_handler('click', self.publish_click)
    self.add_component(self.publush, slot='publish-action')

  def publish_click(self, **event):
    if self.data['cover']: self.data['cover'] = True
    print(self.data)
    work_id = anvil.server.call('work_publish', self.data)
    print(work_id)
    


  def input_change(self, **event):
    #sender = event['sender']
    self.data['type'] = self.type.selected_value
    self.data['title'] = self.title.text
    self.data['uri'] = parse_uri(self.title.text)
    self.uri.text = self.data['uri']
    
    if self.genre.selected_value:
      self.data['genre'] = self.genre.selected_value
      self.subgenre.items = genres.genre_subgenre_names(self.genre.selected_value)
    else:
      self.data['genre'] = None
      self.subgenre.items = []

    if self.subgenre.selected_value:
      self.data['subgenre'] = self.subgenre.selected_value
    else:
      self.data['subgenre'] = None

    if event['sender'] == self.keywords:
      self.data['keywords'].append(self.keywords.text)
      self.keywords.text = ""
      self.keywords_label.icon = 'fa:remove'
      
      self.keywords_label.text = ",".join(self.data['keywords'])

    if event['sender'] == self.keywords_label:
      self.data['keywords'] = []
      self.keywords_label.text = ""
      self.keywords_label.icon = 'fa:tags'

    self.update_cover()


  def auto_type(self):
    parsed = parse_type(self.data['html'])
    prose = genres.prose_by_words(self.data['words'])
    poetry = genres.poetry_by_paragraphs(parsed['paragraphs'])
  
    self.data['types'] = prose + poetry
    if parsed['type'] == 'prose':
      self.data['type'] = prose[0]
    else:
      self.data['type'] = poetry[0]


  def design_change(self, sender, **event):
    contrast = 11
    color = jQ('#color').val()
    background = jQ('#background').val()

    if sender.id == 'font':
      self.data[sender.id] = sender.selected_value

    elif sender.id == 'color':
      background = adjust_color_for_contrast(color, background, contrast)
    elif sender.id == 'background':
      self.cover_file.clear()
      self.cover_file.text = 'корица'
      self.data['cover'] = None

      color = adjust_color_for_contrast(background, color, contrast)
    else:
      self.data[sender.id] = jQ(sender).val()
    
    self.data['shadow'] = adjust_color_for_contrast(color, '000000', 100)
    print('shadow', self.data['shadow'])
    self.data['color'] = color
    self.data['background'] = background
    print(color, background)
    jQ('#color').val(color)
    jQ('#background').val(background)

    self.update_cover()

  def new_cover(self, file, **event):
     self.cover_file.text = file.name
     cover = anvil.image.generate_thumbnail(file, 450)
     content_type = file.content_type
     cover_bytes = cover.get_bytes()
     image_base64 = base64.b64encode(cover_bytes).decode('utf-8')
     image_url = f'data:{content_type};base64,{image_base64}'
     self.data['cover'] = f'url("{image_url}")'
     self.data['cover_base64'] = image_base64
     self.data['cover_mime'] = content_type
     
     self.update_cover()

  def update_cover(self, **event):
    jQ(self.cover).empty()
    cover = cover_non_cached(self.data)
    jQ(self.cover).append(cover())

  def check_data(self, data, *event):
    if not data:
      data = demo
    for key, value in demo.items():
      if key not in data:
          data[key] = value
    return data

demo = {
      'id': 'test_id',
      'title': "Заглавие",
      'uri': "uri",
      'type': "тип",
      'keywords': [],
      'words': 0,
      'cover': False,
      'html': '<p>hello</p>',

}


