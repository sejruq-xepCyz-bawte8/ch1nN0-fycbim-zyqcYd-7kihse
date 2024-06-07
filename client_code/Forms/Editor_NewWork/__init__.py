from anvil import *
from .._FormTemplate import _FormTemplate
from anvil.js.window import jQuery as jQ
from time import time, sleep
from anvil_extras.storage import indexed_db
from .WorkTemplate import WORK_TEMPLATE

from ...PyScript import PyScriptLoader

from time import time
from random import randint
import datetime



META_STORE = indexed_db.create_store('editor_meta')
HTML_STORE = indexed_db.create_store('editor_html')



forward_element = jQ("#navl-Editor-Editor_Work")


class Editor_NewWork(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.pyscript = False
    self.init_components(**properties)

    if 'CURRENT' in META_STORE:
      self.has_current = True
      self.old_work_id = META_STORE['CURRENT']
      self.old_meta = META_STORE[self.old_work_id]
      self.old_html = HTML_STORE[self.old_work_id]
    else:
      self.has_current = False
      self.old_work_id = None
      self.old_meta = {'title': 'Няма текущо отворена'}
      self.old_html = ''
 
    self.action_bar = self.add_flowpanel()
    self.action_empty = self.add_button(text="Нова празна", parent=self.action_bar, click=self.init_new_work)
    self.action_loaded = self.add_button(text="Нова от файла", parent=self.action_bar, click=self.init_new_work)
    self.file_loader = self.add_uploader(change=self.on_upload, text="Отвори файл", parent=self.action_bar)
    self.file_loader.file_types =  '.txt,.md,.docx'
    self.file_loader.enabled = True if PyScriptLoader.PYSCRIPT_FILE_PARSER else False 
    self.emplty_lines = self.add_button(text='2->1 празен ред', click=self.clean_empty)
    

    self.title = self.add_textbox(placeholder='Заглавие на новата (може и после в корица)')
    self.label = self.add_label(text="")
    self.preview_bar = self.add_colpanel()
    self.preview = self.add_rich_html(text="", parent=self.preview_bar)
    self.init_pyscript()

  def show_form(self, **event):
    self.label.text = f"Текуща Творба: {self.old_meta['title']}"
    self.preview.content = self.old_html


  def init_new_work(self, sender=None, html:str=None, **event):
    if sender is self.action_loaded:
      html = self.preview.content
    if not html: html = ""
    self.data = WORK_TEMPLATE

    if self.title.text:
        self.data['title'] = self.title.text
    elif sender is self.action_loaded:
        self.data['title'] = self.file_loader.file.name
    else:
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d-%b-%Y %H:%M")
        self.data['title'] = formatted_date

    self.data['work_id'] = f"{time():.10f}{randint(1000000000, 9999999999)}"
    self.data['ctime'] = time()
    self.data['mtime'] = time()
    self.html_work = html
    work_id = self.data['work_id']
    META_STORE['CURRENT'] = work_id
    META_STORE[work_id] = self.data
    HTML_STORE[work_id] = self.html_work
    
    all_works = META_STORE['ALL'] + [work_id] if 'ALL' in META_STORE else [work_id]
    META_STORE['ALL'] = all_works

    if META_STORE['CURRENT'] == work_id and META_STORE[work_id] == self.data and HTML_STORE[work_id] == self.html_work:
        self.navClick(forward_element)
    else:
        self.label.text('Възникна грешка')
        META_STORE['CURRENT'] = self.old_work_id
        META_STORE[work_id] = self.old_meta
        HTML_STORE[work_id] = self.old_html



  def on_upload(self, sender, **event):
    sender.text = sender.file.name
    extention = sender.file.name.split('.')[-1]
    
    if extention == "txt":
      self.load_txt_file(sender)
    elif extention == "docx":
      self.load_docx_file()
    elif extention == "md":
      self.load_md_file()
  


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
    from anvil.js.window import DOCX_parser
    docx_bytes = self.file_loader.file.get_bytes()
    parsed_docx = DOCX_parser(docx_bytes)
    self.preview_parsed_file(html = parsed_docx)


  def load_md_file(self):
    
    from anvil.js.window import MD_parser
    md_bytes = self.file_loader.file.get_bytes()
    parsed_docx = MD_parser(md_bytes)
    self.preview_parsed_file(html = parsed_docx)

  def clean_empty(self, sender, **event):
    double_empty = '<p></p><p></p>'
    single_empty = '<p></p>'
    dirty = self.preview.content
    clean = dirty.replace(double_empty, single_empty)
    self.preview.content = clean


# PYSCRIPT
  def init_pyscript(self):
    if not PyScriptLoader.PYSCRIPT_FILE_PARSER:
      PyScriptLoader.load_pyscript()
      PyScriptLoader.load_pyscript_files_parser()
    
  def FILES_parser_loaded(self, pyscript, **event):
    self.file_loader.enabled = True
    PyScriptLoader.PYSCRIPT_FILE_PARSER = True













