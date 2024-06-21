from anvil import *
from .._FormTemplate import _FormTemplate
from ...API.ChartsApi import api_charts

class Reader_Charts(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)

    chart = api_charts()
    print(chart)
    





