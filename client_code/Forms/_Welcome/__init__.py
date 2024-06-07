from anvil import *
from .._FormTemplate import _FormTemplate


class _Welcome(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_div(text=self.form_name)
    self.add_div(text="---")
    self.add_div(text="ЧетеМе 0.5.4")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="Тази версия е само за тестване на писателските/авторски форми (без тези за профил и публикуване)")

    
    




