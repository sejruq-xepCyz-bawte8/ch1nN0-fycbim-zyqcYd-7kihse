from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import EDITOR
from ...PyScript.PyScriptLoader import has_pyscript
from anvil_extras import non_blocking
from anvil.js import window




class Author_NewWork(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
  
    self.action_bar = self.add_flowpanel()
    self.action_create = self.add_button(text="Създай", parent=self.action_bar, click=self.make_and_open)
    self.action_clean = self.add_button(text="Изчисти", parent=self.action_bar, click=self.clean_data)
    self.file_loader = self.add_uploader(change=self.on_upload, text="Отвори файл", parent=self.action_bar)
    self.file_loader.file_types =  '.txt,.md,.docx'
    self.file_loader.enabled = True if has_pyscript() else False 
    self.emplty_lines = self.add_button(text='2->1 празен ред', click=self.clean_empty)
    self.title = self.add_textbox(placeholder='Заглавие на новата (може и после в корица)')
    self.label = self.add_label(text="")
    self.preview_bar = self.add_colpanel()
    self.preview = self.add_rich_html(text="", parent=self.preview_bar)

    self.pyscript = non_blocking.repeat(self.check_pyscript, 1)

    self.work_html = '<p>...</p>'

    self.init_components(**properties)


  def show_form(self, **event):
    pass

  def check_pyscript(self):
      if has_pyscript():
          self.file_loader.enabled = True
          self.pyscript.cancel()


  def make_and_open(self, sender=None, html:str=None, **event):
    if sender is self.action_create:
      html = self.preview.content if self.preview.content else '<p>...</p>'
   
    if self.title.text:
        title = self.title.text
    else:
        title = None

    new_work_id = EDITOR.new_work(html=html, title=title)
    if new_work_id : new_current = EDITOR.set_current(work_id=new_work_id)
    if new_current : self.navClick_by_id(link_id="#navl-Editor-Editor_Work", from_group="Author")



  def on_upload(self, sender, **event):
    sender.text = sender.file.name
    extention = sender.file.name.split('.')[-1]
    
    if extention == "txt":
      self.load_txt_file(sender)
    elif extention == "docx":
      self.load_docx_file()
    elif extention == "md":
      self.load_md_file()
  
  def clean_data(self, sender, **event):
    self.preview.content = ''
    self.file_loader.clear()
    self.title.text = ''
    self.label.text = ''

  def load_txt_file(self, sender):
    html:str = ''
    lines:list = []
    file = sender.file
    bytes = file.get_bytes()
    string_content:str = bytes.decode('utf-8')
    lines = string_content.splitlines()
    for line in lines:
        line = f'<p>{line}</p>'
        html += line
    self.preview_parsed_file(html = html)
    

  def preview_parsed_file(self, html):
    self.label.text = f'Превю на {self.file_loader.file.name}'
    self.preview.content = html


  def load_docx_file(self):
    docx_bytes = self.file_loader.file.get_bytes()
    parsed_docx = window.DOCX_parser(docx_bytes)
    self.preview_parsed_file(html = parsed_docx)


  def load_md_file(self):
    md_bytes = self.file_loader.file.get_bytes()
    parsed_docx = window.MD_parser(md_bytes)
    self.preview_parsed_file(html = parsed_docx)

  def clean_empty(self, sender, **event):
    double_empty = '<p></p><p></p>'
    single_empty = '<p></p>'
    dirty = self.preview.content
    clean = dirty.replace(double_empty, single_empty)
    self.preview.content = clean
    














