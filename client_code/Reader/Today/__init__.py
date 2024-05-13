from ._anvil_designer import TodayTemplate
from anvil import *
import anvil.server
import anvil.users

user = anvil.users.get_user()


class Today(TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def click(self, **event):
    print(event)