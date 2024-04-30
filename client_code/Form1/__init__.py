from ._anvil_designer import Form1Template
from anvil import *
from ..Elements import new_card
from ..Elements.Card import Card

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.add_card(10)
    dg = DataGrid(rows_per_page=3)
    drp = DataRowPanel()
    drp.add_component(TextBox)
    rp = RepeatingPanel()
    rp.item_template = DataRowPanel
    rp.items = [1,2,3,4,5,6,7,8,9]
    dg.add_component(rp)
    self.add_component(dg)