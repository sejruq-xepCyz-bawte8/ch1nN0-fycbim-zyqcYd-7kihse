from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import EDITOR




class Editor_Publish(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)
    
  


    self.add_div(text=EDITOR.data.get('title', None))
    self.add_div(text=EDITOR.data.get('published', None))
    self.add_div(text=EDITOR.data.get('genres', None))
    self.add_div(text=EDITOR.data.get('ctime', None))
    self.add_div(text=EDITOR.data.get('uri', None))
    self.add_button(text="Публикувай", click=self.publish)
# check all fields are ok
# check not repeiting uris
# check if not already published same time same data

# all ok then send for publish



  def publish(self, sender, *event):
    pass

