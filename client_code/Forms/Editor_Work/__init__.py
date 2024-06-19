from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Quill import Quill
from anvil_extras import non_blocking

from ...Index.App import EDITOR

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
  
  def show_form(self, **event):

    self.editor = Quill(toolbar=toolbarOptions, sanitize=False)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.add_component(self.editor)

    self.words_count = self.add_label(role="ch-top-right")
    self.words_count.bold = True
      
    self.title_info = self.add_label(text=EDITOR.data['title'])

    self.deferred_change = None
    self.deferred_save = None
    
    self.editor.set_html(EDITOR.html)
    self.words_count.text = EDITOR.data['words']


  def editor_change(self, sender, **event):
    self.words_count.foreground = "Gray"
    non_blocking.cancel(self.deferred_change)
    non_blocking.cancel(self.deferred_save)
    self.deferred_change = non_blocking.defer(self.changes_calc, 1)
    self.deferred_save = non_blocking.defer(self.save_buffer, 3)
    
  def changes_calc(self):
    EDITOR.html = self.editor.get_html()
    text = self.editor.get_text()
    words = len(text.split())
    size = len(text.encode('utf-8'))
    self.words_count.text = words
    EDITOR.data['words'] = words
    EDITOR.data['size'] = size
    self.words_count.foreground = "Blue"
    if size > 1_111_111:
      self.words_count.background = "Red"
    else:
      self.words_count.background = None

  def save_buffer(self):
    updated = EDITOR.update()
    if updated:
      self.words_count.foreground = "Green"
    else:
      self.words_count.foreground = "Red"

    
    


    
    
 





