from ._anvil_designer import Form1Template
from anvil import *
from ..Elements import new_card
from ..Elements.Card import Card

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Create your Data Grid 
    grid = DataGrid()
    grid.rows_per_page = 3
    # Add the Data Grid to your Form
    self.add_component(grid)

    # Add two columns to your Data Grid


    rp = RepeatingPanel(item_template=Card)
    # Set its items property
    rp.items = [1,2,3,4,5,6,7,8,9
    ]
    # Add the repeating panel to your data grid
    grid.add_component(rp)
