from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Quill import Quill
from anvil_extras import non_blocking

from anvil_extras.storage import indexed_db
from time import time

META_STORE = indexed_db.create_store('editor_meta')
HTML_STORE = indexed_db.create_store('editor_html')


toolbarOptions:list = [
  [{ 'header': 1 },
   { 'header': 2 },
   { 'align': 'center' },
   { 'align': 'right' },
    'blockquote',
    'bold',
    'italic',
    'image',
    'clean'
   ],
]


class Editor_Work(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)

    self.work_id = META_STORE['CURRENT'] if 'CURRENT' in META_STORE else None

    self.data = META_STORE[self.work_id]
    self.work_html = HTML_STORE[self.work_id]

    self.editor = Quill(toolbar=toolbarOptions, placeholder="Текст на творбата ...", sanitize=True)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.add_component(self.editor)

    self.words_count = self.add_label(role="ch-top-right")
    self.words_count.bold = True
    
    self.title_info = self.add_label(text=self.data['title'])


    self.deferred_change = None
    self.deferred_save = None
    
    
  def show_form(self, **event):

    if not self.work_id : open_form('Forms.Editor_NewWork')
    
    self.editor.set_html(self.work_html, sanitize=None)
    self.words_count.text = self.data['words']    


  def editor_change(self, sender, **event):
    self.words_count.foreground = "Orange"
    non_blocking.cancel(self.deferred_change)
    non_blocking.cancel(self.deferred_save)
    self.deferred_change = non_blocking.defer(self.changes_calc, 1)
    self.deferred_save = non_blocking.defer(self.save_buffer, 5)
    
  def changes_calc(self):
    self.words_count.foreground = "Blue"
    self.work_html = self.editor.get_html()
    text = self.editor.get_text()
    words = len(text.split())
    self.words_count.text = words
    self.data['words'] = words
    self.data['mtime'] = time()



  def save_buffer(self):
    saved = False
    try:
      HTML_STORE[self.work_id] = self.work_html
      saved = True
    except:
      saved = False

    try:
      META_STORE[self.work_id] = self.data
      saved = True
    except:
      saved = False
    
    if saved:
      self.words_count.foreground = "Green"
    else:
      self.words_count.foreground = "Red"

    
    


    
    
 





