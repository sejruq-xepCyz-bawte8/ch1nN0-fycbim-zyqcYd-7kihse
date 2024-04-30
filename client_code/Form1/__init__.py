from ._anvil_designer import Form1Template
from anvil import *
from ..ElementsHtml.Icon import Icon
from time import sleep

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    icon = Icon()
    target = self.dom_nodes['ch-form']
    print(target)
    target.appendChild(icon())

    icon.text = "tesasdasdasdasdt"
    


