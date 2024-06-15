from anvil import *
from .._FormTemplate import _FormTemplate
from ...API.ReaderApi import api_author


class ViewerA_Author(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    #self.uri = get_url_hash()
    #self.author_uri = self.uri.get('author')
    
    self.init_components(**properties)
    #data, html = api_author(self.author_uri)
    #self.data = data
    #self.author_html = html

  def show_form(self, **event):
    if self.data:
      self.add_div(text=self.data['author_name'])
      author_info = self.add_div()
      author_info.html(self.author_html)
    else:
      self.add_div(text=f'No author with uri {self.uri}')
    
    

    
    




