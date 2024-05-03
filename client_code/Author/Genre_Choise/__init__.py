from ._anvil_designer import Genre_ChoiseTemplate
from anvil import *
from anvil_extras import ChipsInput
from ...Cheteme.Memory import genres
from ...Cheteme.Memory import awesome

print(genres.get_all_in_level(1))

class Genre_Choise(Genre_ChoiseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.genres_l1 = FlowPanel()
    self.genres_l2 = FlowPanel()
    self.genres_l3 = FlowPanel()
    self.add_component(self.genres_l1)
    self.add_component(self.genres_l2)
    self.add_component(self.genres_l3)
    l1 = genres.get_all_in_level(1)
    l2 = genres.get_all_in_level(2)
    l3 = genres.get_all_in_level(3)

    self.add_chips(l1, self.genres_l1)
    self.add_chips(l2, self.genres_l2)
    self.add_chips(l3, self.genres_l3, filter="all")

  def add_chips(self, level, container, filter=None):
    for l in level:
      chip = ChipsInput.Chip()
      chip.text = l['bg']
      icon = awesome.get_icon_code(l['bg'])
      chip.icon = f'fa:{icon}'
      chip.close_icon = None
      chip.selected = False
      chip.add_event_handler('click', self.l0_click)
      container.add_component(chip)

  
  def l0_click(self, **event):
    sender = event['sender']
    components = sender.parent.get_components()
    
    if not sender.selected:
      for c in components:
        if c != sender :
          c.visible = False
        else:
          c.visible = True
          c.background = 'lightgreen'
          c.close_icon = 'x'
          c.selected = True
    else:
      for c in components:
          c.visible = True
          c.background = None
          c.close_icon = None
          c.selected = False
      
