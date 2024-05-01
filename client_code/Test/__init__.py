from ._anvil_designer import TestTemplate
from anvil import *
from ..ElementsHtml.Icon import Icon
from time import sleep

class Test(TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    icon = Icon()
    target = self.dom_nodes['ch-form']
    print(target)
    target.appendChild(icon())

    icon.text = "123"
    


