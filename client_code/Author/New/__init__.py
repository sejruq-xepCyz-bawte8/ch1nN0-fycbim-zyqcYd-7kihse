from ._anvil_designer import NewTemplate
from anvil import *
from ...Cheteme.ElementsHtml.Icon import Icon
from anvil_extras import ChipsInput
import anvil.js

class New(NewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.quill = None

    

  def post(self, *event):
    if not self.quill :
      from anvil.js.window import quill
      self.quill = quill
    self.words = int(self.dom_nodes['counter'].innerText)
    self.text = self.quill.getText()
    self.html_content = self.quill.getSemanticHTML()
    
    print(self.words, self.html_content)
    

    # Any code you write here will run before the form opens.



