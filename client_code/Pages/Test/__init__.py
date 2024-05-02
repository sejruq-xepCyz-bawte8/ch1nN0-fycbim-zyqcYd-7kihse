from ._anvil_designer import TestTemplate
from anvil import *
from ...About import About
from anvil_extras import routing


@routing.default_template
class Test(TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.content_panel = ColumnPanel()
    self.add_component(self.content_panel)
    self.init_components(**properties)

    


