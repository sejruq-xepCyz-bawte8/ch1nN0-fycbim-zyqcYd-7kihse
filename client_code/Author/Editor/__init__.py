from ._anvil_designer import EditorTemplate
from ...Cheteme.Main import navigation_click
from anvil import *


class Editor(EditorTemplate):
  def __init__(self, **properties):
    self.navigation_click = navigation_click
    self.init_components(**properties)

  def post(self, *event):
    from anvil.js.window import quill
    data = {
      'words': int(self.dom_nodes['counter'].innerText),
      'html': quill.getSemanticHTML()
    }
    
    open_form('Author.Publish', data)




