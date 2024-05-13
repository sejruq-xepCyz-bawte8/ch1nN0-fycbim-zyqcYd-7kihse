from ._anvil_designer import ProfileTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Profile(ProfileTemplate):
  def __init__(self, **properties):
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
