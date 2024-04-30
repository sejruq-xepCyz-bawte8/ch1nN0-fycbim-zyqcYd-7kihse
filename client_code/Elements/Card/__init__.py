from ._anvil_designer import CardTemplate
from anvil import *
from ...Works import get_work



class Card(CardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    work = get_work(self.work_id)
    self.title.text = work['title']
    self.image_1.source = "_/theme/chetemecover.webp"
    print(self.work_id)
    # Any code you write here will run before the form opens.
