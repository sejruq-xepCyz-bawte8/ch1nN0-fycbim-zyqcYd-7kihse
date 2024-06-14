from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import EDITOR
from ...Index.App import USER_ID
import anvil.server
from time import sleep

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



  def publish(self, sender, **event):
    print('publush click')

    if USER_ID:
      print('publush calling')
      task = anvil.server.call('publish_author_work', html=EDITOR.html, data=EDITOR.data)
      query = self.add_label()
      for t in range(60):
        sleep(1)
        query.text=task.get_state()['message']
        if task.is_completed(): break
      result = task.get_return_value()
      if result:
         self.add_div(text='ГОТОВО всичко е успешно')
  
      else:
         self.add_div(text='ПРИКЛЮЧИ но с грешки')

