from ._anvil_designer import TodayTemplate
from anvil import *



class Today(TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
