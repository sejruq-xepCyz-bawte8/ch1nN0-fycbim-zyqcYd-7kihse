from ._anvil_designer import NewTemplate
from anvil import *
from ...Cheteme.ElementsHtml.Icon import Icon
from anvil_extras import ChipsInput
from anvil.js.window import Quill

class New(NewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    editor = self.dom_nodes['editor']
    self.quill = Quill( editor, {
        'modules': {
          'toolbar': "#toolbar",
          'counter': {'container': '#counter','unit': 'word'},
          
        },
        'theme': 'snow'
    })
    

  def post(self, *event):
    self.words = int(self.dom_nodes['counter'].innerText)
    self.text = self.quill.getText()
    #self.html = self.quill.getSemanticHTML()
    print(self.html)
    print(self.words)
    

    # Any code you write here will run before the form opens.



