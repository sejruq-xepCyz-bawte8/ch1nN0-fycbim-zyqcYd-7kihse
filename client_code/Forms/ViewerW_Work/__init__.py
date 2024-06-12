from anvil import *
from .._FormTemplate import _FormTemplate


class ViewerW_Work(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)

    
    
  def click_cover(self):
    print('clic_cover')

  def click_toc(self):
    print('clic_toc')

  def click_bookmark(self):
    print('clic_bookmark')

  def click_like(self):
    print('clic_like')



