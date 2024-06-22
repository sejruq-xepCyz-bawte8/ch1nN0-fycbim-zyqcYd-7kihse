from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
from anvil.js.window import jQuery as jQ

class ViewerW_Engage(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_div(text=App.READER.data.get('title'))
    
    self.add_div(text='Харесвания')
    self.add_div(text='Коментари')
    
    self.comment = TextArea(placeholder='Вашият коментар...')
    self.add_component(self.comment)
    self.comment_button = Link(icon = 'fa:comment')
    self.add_component(self.comment_button)
    self.like_button = Link(icon = 'fa:heart')
    self.add_component(self.like_button)
    engagement:list = ['like'] #wid	engage_id	-> open	read	like	comment	text	<- data
    comment:str=None
    App.ENGAGE.my_engage(wid=App.READER.work_id, engagement=engagement, comment=comment)