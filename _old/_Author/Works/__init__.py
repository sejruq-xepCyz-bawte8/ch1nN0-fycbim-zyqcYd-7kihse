from ._anvil_designer import WorksTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Works(WorksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from ..._Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
