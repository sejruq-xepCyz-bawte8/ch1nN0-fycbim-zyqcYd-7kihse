from ._anvil_designer import NewTemplate
from anvil import *
from ...Cheteme.Memory import genres, keywords, awesome
from ...Cheteme.Author.ParseUri import parse_uri
from ...Cheteme.Author.DetectType import parse_type
from ...Cheteme.ElementsHtml.Icon import Icon
from ...Cheteme.ElementsHtml import cover_factory
from anvil_extras import Autocomplete
from anvil.js.window import jQuery as jQ


class New(NewTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.quill = None
    self.data = {
      'title': "Заглавие",
      'uri': "uri",
      'type': "тип",
      'genre': "жанр",
      'subgenre': "поджанр",
      'keywords': [],
      'words': 0,
    }
    #self.publish_container.visible = False

    # PANELS
    self.publish_container = ColumnPanel()
    self.actions = FlowPanel()
    self.input_container = ColumnPanel()
    self.result_container = ColumnPanel()
    
    
    # INPUTS
    self.upload_cover = FileLoader(text = "обложка")
    self.upload_cover.add_event_handler('change', self.new_cover)

    self.type = DropDown(placeholder = 'тип', include_placeholder=True)
    self.type.add_event_handler('change', self.type_change)
    
    self.genre = DropDown(placeholder = 'жанр', include_placeholder=True)
    self.genre.add_event_handler('change', self.genre_change)
    self.genre.items = genres.genre_names_in_level(2)
   
    self.subgenre = DropDown(placeholder = 'поджанр', include_placeholder=True)
    self.subgenre.add_event_handler('change', self.subgenre_change)
    
    self.keywords = Autocomplete.Autocomplete(placeholder = 'ключови думи', include_placeholder=True)
    self.keywords.add_event_handler('suggestion_clicked', self.keywords_change)
    self.keywords.add_event_handler('pressed_enter', self.keywords_change)
    self.keywords.suggestions = keywords.get_column('bg')

    
    self.input_container.add_component(self.type)
    self.input_container.add_component(self.genre)
    self.input_container.add_component(self.subgenre)
    self.input_container.add_component(self.keywords)
    self.input_container.add_component(self.upload_cover)
    

    # ACTIONS
    self.save_draft = Link(icon='fa:save')
    self.save_publish = Link(icon='fa:rss')
    self.back_edit = Link(icon='fa:typewriter')
    self.actions.add_component(self.save_draft)
    self.actions.add_component(self.save_publish)
    self.actions.add_component(self.back_edit)

    # RESULTS
    self.cover = Image(width = "5rem", height = "5rem")
    self.uri = Label()

    self.result_container.add_component(self.cover)
    self.result_container.add_component(self.uri)



    # Master CONTAINER
    self.publish_container.add_component(self.actions)
    self.publish_container.add_component(self.input_container)
    self.publish_container.add_component(self.result_container)

    self.add_component(self.publish_container, slot='default')
  
  def type_change(self, **event):
     self.data['type'] = self.type.selected_value

  def new_cover(self, file, **event):
     self.cover.source = file

  def genre_change(self, **event):
    self.data['genre'] = self.genre.selected_value
    self.subgenre.items = genres.genre_subgenre_names(self.genre.selected_value)
    self.update_result()  

  def subgenre_change(self, **event):
    self.data['subgenre'] = self.subgenre.selected_value
    self.update_result()  

  def keywords_change(self, **event):
    self.data['keywords'].append(self.keywords.text)
    self.keywords.text = ""
    
    self.update_result()  



  def post(self, *event):
    self.editor = self.dom_nodes['editor-container']
    
    self.data['title'] = self.dom_nodes['title'].innerText
    self.data['uri'] = parse_uri(self.data['title'])
    
    #jQ(self.editor).hide()
    if not self.quill :
      from anvil.js.window import quill
      self.quill = quill
    self.words = int(self.dom_nodes['counter'].innerText)
    self.data['words'] = self.words
    #self.text = self.quill.getText()
    self.html_content = self.quill.getSemanticHTML()
    self.auto_type()
    self.update_result()
 


  def auto_type(self, *event):
    parsed = parse_type(self.html_content)
    prose = genres.prose_by_words(self.words)
    poetry = genres.poetry_by_paragraphs(parsed['paragraphs'])
    self.type.items = prose + poetry
    if parsed['type'] == 'prose':
      self.type.selected_value = prose[0]
    else:
      self.type.selected_value = poetry[0]


  

  def update_result(self):
    self.cover = self.dom_nodes['cover']
    cover = cover_factory(self.data)
    jQ(self.cover).append(cover())
    print(cover)
    pass





