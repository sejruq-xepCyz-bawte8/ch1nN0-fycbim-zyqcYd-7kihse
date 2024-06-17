from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Quill import Quill
from anvil_extras.Tabs import Tabs
from anvil.js.window import jQuery as jQ
import anvil.image
import base64
from ...Index.App import USER_ID
import anvil.server
from anvil_extras.storage import indexed_db
from time import sleep
from .Zod_Parse import uri_zod, author_name_zod

toolbarOptions:list = [
  [{ 'header': 1 },
   { 'header': 2 },
   { 'align': 'center' },
   { 'align': 'right' },
   { 'list': 'ordered'},
   { 'list': 'bullet' },
    'blockquote',
    'bold',
    'italic',
    'link',
    'image',
    'clean'
   ],
]

class Author_Profile(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.store_author = indexed_db.create_store('author_profile')
    if 'data' in self.store_author:
      self.data = self.store_author['data']
    else:
      self.data = {'author_name':'', 'author_uri':'','description':'', 'background-image':''}
    if 'html' in self.store_author:
      self.html_author = self.store_author['html']
    else:
      self.html_author = '<p>За автора ...</p>'
    


  def tab_click(self, sender, **event):
    tab = sender.active_tab_index
    self.about_panel.visible = True if tab == 0  else False
    self.info_panel.visible = True if tab == 1  else False
   
  def show_form(self, **event):
    #self.add_label(text=self.form_name)

    #TABS
    self.tabs = Tabs(tab_titles=['За Автора', 'Пермалинк']) #tab_click
    self.tabs.add_event_handler('tab_click', self.tab_click)
    self.add_component(self.tabs)

    # ABOUT PANEL
    self.about_panel = self.add_colpanel()
    self.editor = Quill(toolbar=toolbarOptions, sanitize=True)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.editor.set_html(self.html_author)
    self.about_panel.add_component(self.editor)
    
    # INFO PANEL

    #NAME AND URI AND IMAGE
    self.info_panel = self.add_colpanel(visible=False)

    self.name_group = self.add_flowpanel(parent=self.info_panel)
    self.add_label(text="Имена:", parent=self.name_group)
    self.author_name = self.add_textbox(text=self.data['author_name'], parent=self.name_group, placeholder="Имена Автор", change=self.change_data)


    self.description_group = self.add_flowpanel(parent=self.info_panel)
    self.add_label(text="Кратко инфо:", parent=self.description_group)
    self.description = self.add_textbox(text=self.data['description'], parent=self.description_group, placeholder="Кратко инфо", change=self.change_data)

    self.uri_group = self.add_flowpanel(parent=self.info_panel)
    self.add_label(text="Пермалинк път:", parent=self.uri_group)
    self.author_uri = self.add_textbox(text=self.data['author_uri'], parent=self.uri_group, placeholder="tova-sled-cheteme", change=self.change_data)
    
    self.uri_preview = self.add_label(parent=self.info_panel, text=f"Пермалинк превю - https://chete.me/{self.data['author_uri']}")


    self.image_group = self.add_flowpanel(parent=self.info_panel)
    self.uploader = self.add_uploader(text='Зареди изображение', parent=self.image_group, change=self.tumbnail_gen)
    self.add_button(text='Изчисти изображението', parent=self.image_group)

    self.cover = self.add_image(parent=self.image_group)
    self.cover.display_mode = 'shrink_to_fit'
    self.cover.width = 60
    if self.data['background-image']:
      image_parts = self.data['background-image'].split(';base64,')
      image_bytes = base64.b64decode(image_parts[-1])
      image_mime = image_parts[0].split('data:')[0]
      image = anvil.BlobMedia(content_type=image_mime, content=image_bytes, name="cover.png")
      self.cover.source = image
    

    self.publish_group = self.add_flowpanel(parent=self.info_panel)
    self.publish_button = self.add_button(parent=self.publish_group, text="Публикувай промените...", click= self.publish)

    uri_zod(self.author_uri)
    author_name_zod(self.author_name)


  def change_data(self, sender, **event):
    uri_zod(self.author_uri)
    author_name_zod(self.author_name)
    self.uri_preview.text = f"Пермалинк превю - https://chete.me/{self.author_uri.text}"
    self.data['author_name'] = self.author_name.text
    self.data['description'] = self.description.text
    self.data['author_uri'] = self.author_uri.text
    self.store_author['data'] = self.data
    

  def delete_tumbnail(self, sender, **event):
    self.data['background-image'] = ''
    self.cover.source = None
    self.uploader.text = "Зареди изображение"


  def tumbnail_gen(self, file, **event):
    self.cover.source = file
    self.data['background-image'] = self.parse_cover_image(file)
    self.store_author['data'] = self.data

  def editor_change(self, sender, **event):
    self.html_author = self.editor.get_html()
    self.store_author['html'] = self.editor.get_html()
    


    
        
  def parse_cover_image(self, file, **event)->str:
      cover = anvil.image.generate_thumbnail(file, 450)
      content_type = file.content_type
      cover_bytes = cover.get_bytes()
      image_base64 = base64.b64encode(cover_bytes).decode('utf-8')
      image_url = f'data:{content_type};base64,{image_base64}'
      return image_url
  
  def publish(self, sender, **event):
    print('publush click')

    if USER_ID:
      print('publush calling')
      task = anvil.server.call('update_author_profile', html=self.html_author, data=self.data)
      query = self.add_label()
      for t in range(60):
        sleep(1)
        query.text=task.get_state()['message']
        if task.is_completed(): break
      result = task.get_return_value()
      if result:
         self.add_div(text='ГОТОВО всичко е успешно')
  
      else:
         self.add_div(text='ПРИКЛЮЧИ но с грешки')