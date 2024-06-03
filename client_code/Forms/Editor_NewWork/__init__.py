from anvil import *
from .._FormTemplate import _FormTemplate
from anvil.js.window import jQuery as jQ
from time import time

from anvil_extras.storage import indexed_db

forward_element = jQ("#navl-Editor-Editor_Work")

class Editor_NewWork(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)

    self.editor_store = indexed_db.create_store('editor')

    self.editor_store['html'] = ''
    self.editor_store['words'] = 0
    self.editor_store['cover'] = ''
    self.editor_store['title'] = ''
    self.editor_store['genres'] = []
    self.editor_store['keywords'] = []

    self.editor_store['work_id'] = ''
    self.editor_store['ctime'] = time()
    self.editor_store['mtime'] = time()
    self.editor_store['published'] = False


  def show_form(self, **event):

    self.navClick(forward_element)
    
  def check_for_work(self):
    html = self.editor_store['html'] if 'html' in self.editor_store else None
    title = self.editor_store['title'] if 'title' in self.editor_store else None
    words = self.editor_store['words'] if 'words' in self.editor_store else None
    ctime = self.editor_store['ctime'] if 'ctime' in self.editor_store else None
    mtime = self.editor_store['mtime'] if 'mtime' in self.editor_store else None
    published = self.editor_store['published'] if 'published' in self.editor_store else None
    



