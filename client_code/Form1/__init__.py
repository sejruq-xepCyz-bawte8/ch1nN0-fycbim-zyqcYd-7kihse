from ._anvil_designer import Form1Template
from anvil import *
from ..Elements.Card import Card

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    card = Card(work_id='testid')
   
    self.add_component(card)
    # Any code you write here will run before the form opens.
