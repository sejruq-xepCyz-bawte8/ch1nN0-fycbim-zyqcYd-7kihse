from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import READER

class Reader_Today(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)
    for w in READER.today:
      work_data = READER.get_work_data(wid=w['wid'])
      self.add_div(text=work_data['title'])
    
    





