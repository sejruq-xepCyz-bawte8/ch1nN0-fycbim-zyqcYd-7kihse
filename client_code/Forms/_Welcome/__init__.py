from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import READER


class _Welcome(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
   
    
    self.uri = get_url_hash()
    #self.uris = self.uri.split('/')
    self.init_components(**properties)



  def show_form(self, **event):
    self.add_div(text=self.form_name)
    if 'author' in self.uri:
      self.navClick_by_id("#navl-Reader-ViewerA_Author")
    #if len(self.uris) == 1 and self.uri != '':
      
    if 'work' in self.uri:
      READER.set_current_work(self.uri['work'])
      self.navClick_by_id("#navl-Reader-ViewerW_Work")

 
    self.add_div(text="ЧетеМе 0.6.9")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="Тази версия е само за тестване на писателския пълен цикъл")



