from ._anvil_designer import BookmarksTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Bookmarks(BookmarksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
