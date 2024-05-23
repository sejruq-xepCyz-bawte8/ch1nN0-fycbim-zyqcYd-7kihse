from ._anvil_designer import EditorTemplate
from ..._Cheteme.Main import navigation_click
from anvil import *
from time import time

from ..._Cheteme.Main import user

class Editor(EditorTemplate):
  def __init__(self, **properties):
    self.navigation_click = navigation_click
    #print(sha256("Hello World!"))
    #self.add_event_handler('show', self.form_show)
    self.init_components(**properties)


  def post(self, *event):
    from anvil.js.window import quill
    
    work_id = None


    words = int(self.dom_nodes['counter'].innerText)
    html_content = quill.getSemanticHTML()


    data = {
      'wid': work_id,
      'words': words,
      'html': html_content
    }
    print(data)
    open_form('Author.Publish', data)




