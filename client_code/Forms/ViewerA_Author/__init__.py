from anvil import *
from .._FormTemplate import _FormTemplate
from ...API.ReaderApi import api_author


class ViewerA_Author(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.uri = get_url_hash()
    
    self.init_components(**properties)
    data, html = api_author('beach')
    self.data = data
    self.author_html = html

  def show_form(self, **event):
    
    self.add_div(text=self.data['author_name'])
    author_info = self.add_div()
    author_info.html(self.author_html)
    
    

    
    




