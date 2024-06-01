from anvil import *
from .._FormTemplate import _FormTemplate


class Settings_User(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)

    
    





