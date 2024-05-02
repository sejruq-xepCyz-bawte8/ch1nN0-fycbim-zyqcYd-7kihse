from ._anvil_designer import Form1Template
from anvil import *



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    from anvil.js.window import performance
    from time import time
    tp = performance.timeOrigin
    t0 = time()
    lapp = t0-tp/1000
    print("module after open", lapp)
