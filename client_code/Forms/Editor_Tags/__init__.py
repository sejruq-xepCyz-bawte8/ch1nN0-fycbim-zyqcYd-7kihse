from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.storage import indexed_db

class Editor_Tags(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.editor_store = indexed_db.create_store('editor')
    self.words = self.editor_store['words']
    print(self.words)

  def show_form(self, **event):
    self.add_label(text=self.form_name)

    






