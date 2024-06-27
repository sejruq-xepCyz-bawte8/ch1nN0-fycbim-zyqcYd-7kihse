from ._anvil_designer import StandartFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StandartForm(StandartFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rich_text_1.content
    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass

  def check_box_1_change(self, **event_args):
    self.button_1.enabled = self.check_box_1.checked
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
