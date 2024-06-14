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
      self.html_author = ''
    

  def tab_click(self, sender, **event):
    tab = sender.active_tab_index
    self.about_panel.visible = True if tab == 0  else False
    self.name_panel.visible = True if tab == 1  else False
   
  def show_form(self, **event):
    #self.add_label(text=self.form_name)

    #TABS
    self.tabs = Tabs(tab_titles=['За Автора', 'Пермалинк']) #tab_click
    self.tabs.add_event_handler('tab_click', self.tab_click)
    self.add_component(self.tabs)

    #AUTHOR ABOUT
    self.about_panel = self.add_colpanel()
    
    self.editor = Quill(toolbar=toolbarOptions, placeholder="За Автора ...", sanitize=True)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.editor.set_html(self.html_author)

    self.about_panel.add_component(self.editor)
    

    #NAME AND URI AND IMAGE
    self.name_panel = self.add_colpanel(visible=False)
    self.author_name = self.add_textbox(text=self.data['author_name'], parent=self.name_panel, placeholder="Имена Автор", change=self.change_data)
    self.description = self.add_textbox(text=self.data['description'], parent=self.name_panel, placeholder="Descr", change=self.change_data)
    self.uri_panel = self.add_flowpanel(parent=self.name_panel)
    self.add_label(parent=self.uri_panel, text='Пермалинк: chete.me/')
    self.author_uri = self.add_textbox(text=self.data['author_uri'], parent=self.uri_panel, placeholder="vasia-cheteme-link", change=self.change_data)
   
    
    self.uploader = self.add_uploader(parent=self.name_panel, change=self.tumbnail_gen)
    self.cover = self.add_image(parent=self.name_panel)
    self.publish_button = self.add_button(parent=self.name_panel, text="Публикувай промените...", click= self.publish)

  def change_data(self, sender, **event):
    self.data['author_name'] = self.author_name.text
    self.data['description'] = self.description.text
    self.data['author_uri'] = self.author_uri.text
    self.store_author['data'] = self.data
    
  def tumbnail_gen(self, file, **event):
    self.data['background-image'] = self.parse_cover_image(file)
    self.store_author['data'] = self.data

  def editor_change(self, sender, **event):
    self.html_author = self.editor.get_html()
    self.store_author['html'] = self.editor.get_html()
    

  def publish(self, sender, **event):
    print('publush click')

    if USER_ID:
      print('publush calling')
      task = anvil.server.call('update_author_profile', html=self.html_author, data=self.data)
      for t in range(20):
        sleep(1)
        self.add_div(text=task.get_state())
        if task.is_completed(): break
      self.add_div(text=f'Резултат task.get_return_value()')
        



  def parse_cover_image(self, file, **event)->str:
      cover = anvil.image.generate_thumbnail(file, 450)
      content_type = file.content_type
      cover_bytes = cover.get_bytes()
      image_base64 = base64.b64encode(cover_bytes).decode('utf-8')
      image_url = f'data:{content_type};base64,{image_base64}'
      #url = f'url("{image_url}")'
      #bytes = image_base64
      #mime = content_type
      return image_url