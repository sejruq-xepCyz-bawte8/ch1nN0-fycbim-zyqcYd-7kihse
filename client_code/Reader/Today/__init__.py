from ._anvil_designer import TodayTemplate
from ...Cheteme.Main import navigation_click
from anvil.js.window import jQuery as jQ
from anvil import *
import anvil.server
import anvil.users
from ...Cheteme.ElementsHtml.panels_module import create_panel
user = anvil.users.get_user()


class Today(TodayTemplate):
  def __init__(self, **properties):
    self.navigation_click = navigation_click
    self.init_components(**properties)
    self.add_event_handler('show', self.show_form)
  def show_form(self, **event):
    n = 30
    create_panel(target_id="#published", n=n, engagement='p')
    create_panel(target_id="#readed", n=n, engagement='r', period='d')
    create_panel(target_id="#liked", n=n, engagement='l', period='d')
  



    # Any code you write here will run before the form opens.
  def click(self, **event):
    print(event)