from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App


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
    
    self.add_div(text=App.READER.author_data['author_name'])
    author_info = self.add_div()
    author_info.html(App.READER.author_html)

    
    

    
    




