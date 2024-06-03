from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Quill import Quill

from anvil_extras.storage import indexed_db




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
    
    self.editor = Quill(toolbar=toolbarOptions, placeholder="Текст на творбата ...", sanitize=True)
    self.editor.add_event_handler('text_change', self.editor_change)
    self.words_count = self.add_label(text=0, role="ch-top-right")
    
    self.editor_store = indexed_db.create_store('editor')
    
    

    


  def editor_change(self, sender, **event):
    self.editor_store['html'] = sender.get_html()
    text = sender.get_text()
    words = len(text.split())
    self.words_count.text = words
    self.editor_store['words'] = words
    
  def show_form(self, **event):
    if not 'html' in self.editor_store : open_form('Forms.Editor_NewWork')
    self.add_component(self.editor)
    self.editor.set_html(self.editor_store['html'], sanitize=None)
    self.words_count.text = self.editor_store['words']

    
    
 





