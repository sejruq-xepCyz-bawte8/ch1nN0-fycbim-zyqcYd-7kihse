from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.Main import VER

class Settings_Info(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=f'ЧетеМе - {VER}')

    
    





