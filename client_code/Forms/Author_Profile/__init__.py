from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Quill import Quill
from anvil_extras.Tabs import Tabs
from anvil.js.window import jQuery as jQ


toolbarOptions_:list = [
  ['bold', 'italic', 'underline', 'strike'],        # toggled buttons
  ['blockquote', 'code-block'],
  ['link', 'image', 'video', 'formula'],

  [{ 'header': 1 }, { 'header': 2 }],               # custom button values
  [{ 'list': 'ordered'}, { 'list': 'bullet' }, { 'list': 'check' }],
  [{ 'script': 'sub'}, { 'script': 'super' }],      # superscript/subscript
  [{ 'indent': '-1'}, { 'indent': '+1' }],          # outdent/indent
  [{ 'direction': 'rtl' }],                         # text direction

  [{ 'size': ['small', 'false', 'large', 'huge'] }],  # custom dropdown
  [{ 'header': [1, 2, 3, 4, 5, 6, 'false'] }],

  [{ 'color': [] }, { 'background': [] }],          # dropdown with defaults from theme
  [{ 'font': [] }],
  [{ 'align': [] }],

  ['clean']                                         # remove formatting button
]

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
    

  def tab_click(self, sender, **event):
    tab = sender.active_tab_index
    self.about_panel.visible = True if tab == 0  else False
    self.name_panel.visible = True if tab == 1  else False
   


  def show_form(self, **event):
    #self.add_label(text=self.form_name)

    #TABS
    self.tabs = Tabs(tab_titles=['За Автора', 'Име, Линк и Кавър']) #tab_click
    self.tabs.add_event_handler('tab_click', self.tab_click)
    self.add_component(self.tabs)

    #AUTHOR ABOUT
    self.about_panel = self.add_colpanel()
    
    self.editor = Quill(toolbar=toolbarOptions, placeholder="За Автора ...", sanitize=True)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.about_panel.add_component(self.editor)
    

    #NAME AND URI AND IMAGE
    self.name_panel = self.add_colpanel(visible=False)
    self.author_name = self.add_textbox(parent=self.name_panel, placeholder="Имена Автор")
    self.add_label(parent=self.name_panel, text='chete.me/линк_автор_на_латиница')
    self.author_url = self.add_textbox(parent=self.name_panel, placeholder="линк автор")
    self.uri_generate = self.add_button(parent=self.name_panel, text="Генерирай линк от името")
    self.uri_check = self.add_button(parent=self.name_panel, text="Провери линка за уникалност")

    self.uploader = self.add_uploader(parent=self.name_panel)
    self.cover = self.add_image(parent=self.name_panel)
    


  def editor_change(self, sender, **event):
    print('editor changed')
    #html = self.about.get_html()
    text = self.about.get_text()
    print(text)
    words = text.split()
    print('word count', len(words))

  def parse_editor_images(self, html):
    all_images = jQ(".ql-editor img")
    parsed_images = jQ(".ql-editor img.parsed")
    not_parsed_images = jQ(".ql-editor img:not(.parsed)") 
    print("images", len(all_images), len(parsed_images), len(not_parsed_images))
    for image in not_parsed_images:
      self.parse_image(image)
   

  def parse_image(self, image_el):
    print('parse_image', image_el)
    #image_el.addClass('parsed')