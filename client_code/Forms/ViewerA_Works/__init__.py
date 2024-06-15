from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import READER


class ViewerA_Works(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    


  def show_form(self, **event):
    self.add_label(text=self.form_name)
    # Set Form properties and Data Bindings.
    #self.reader = self.dom_nodes['cheteme_reader']
    works = READER.author_data.get('works')
    for key in works.keys():
      self.add_div(text=key)
