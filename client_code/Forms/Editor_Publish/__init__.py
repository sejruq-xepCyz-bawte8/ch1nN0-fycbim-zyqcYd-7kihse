from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
import anvil.server
from time import sleep, time


class Editor_Publish(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)
    
  


    self.add_div(text=App.EDITOR.data.get('title', None))
    self.add_div(text=App.EDITOR.data.get('published', None))
    self.add_div(text=App.EDITOR.data.get('genres', None))
    self.add_div(text=App.EDITOR.data.get('ctime', None))
    self.add_div(text=App.EDITOR.data.get('uri', None))
    self.add_button(text="Публикувай", click=self.publish)
# check all fields are ok
# check not repeiting uris
# check if not already published same time same data

# all ok then send for publish



  def publish(self, sender, **event):
    self.add_div('Започна публикуването, изчакайте за резултата ...')
    print('publush click')

    if App.USER_ID:
      print('publush calling')
      App.EDITOR.data['ptime'] = time()
      task = anvil.server.call('publish_author_work', html=App.EDITOR.html, data=App.EDITOR.data)
  
      for t in range(60):
        sleep(3)
        if task.is_completed(): break
      result = task.get_return_value()
      if result:
         self.add_div(text='ГОТОВО всичко е успешно')
      else:
         self.add_div(text='ПРИКЛЮЧИ но с грешки')

