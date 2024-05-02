from ._anvil_designer import AboutTemplate
from anvil import *
from time import time


class About(AboutTemplate):
  def __init__(self, t0, **properties):
    # Set Form properties and Data Bindings.
    self.t0 = t0
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    t1 = time()
    dt = t1 - self.t0
    print(self.t0)
    print(t1)
    print(dt)
