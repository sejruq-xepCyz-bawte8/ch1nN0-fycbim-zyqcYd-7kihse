from ._anvil_designer import EditorTemplate
from anvil import *


class Editor(EditorTemplate):
  def __init__(self, **properties):
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)
    #self.add_event_handler('show', self.form_show)


  def form_show(self, *event):
    pass

  def post(self, *event):
    from anvil.js.window import quill
    data = {
      'words': int(self.dom_nodes['counter'].innerText),
      'html': quill.getSemanticHTML()
    }
    
    open_form('Author.Publish', data)




