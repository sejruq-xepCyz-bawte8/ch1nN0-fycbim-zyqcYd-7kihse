from anvil import *
from .._FormTemplate import _FormTemplate


class _Welcome(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_div(text=self.form_name)
    self.add_div(text="---")
    self.add_div(text="ЧетеМе 0.4")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="---")
    self.add_div(text="Тази версия е само за тестване и има елементи в интерфейса, които после няма да ги има или да излизат :) като Творбата тук горе вдясно и Писателя долу (активен само за регистрирани като писател после)")

    
    




