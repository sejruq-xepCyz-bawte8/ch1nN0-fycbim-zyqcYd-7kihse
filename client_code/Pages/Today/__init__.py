from ._anvil_designer import TodayTemplate
from anvil import *
from anvil.js.window import loki
from time import time
# need to have 3 panels - Last 20, Readed and Liked for last 24 hours aka today
# panel > header + slider ; slider > cards 

panels = [
  {'title':'Последни', 'register':'published', 'timeframe': 'all', 'volume': 20},
  {'title':'Най-четени', 'register':'reads', 'timeframe': '24', 'volume': 20},
  {'title':'Най-харесвани', 'register':'likes', 'timeframe': '24', 'volume': 20}
]

class Today(TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    db = loki("test.db")
    items = db.addCollection('items')
    items.insert(panels)
    for r in range (1000):
      d = {'title':'Последни', 'register':'published', 'timeframe': 'all', 'volume': r}
      items.insert(d)
    t1 = time()
    mydv = items.addDynamicView('test')
    mydv.applyFind({ 'title' : 'Последни' })
    "function(obj) { return obj.name === 'Toyota'; }"
    mydv.applyWhere(query).count()
    tyrfing = items.chain().find().where(query).count()
    t2 = time()
    print(tyrfing)
    print(t2-t1)
    # Any code you write here will run before the form opens.


def query(obj):
  return obj.volume >=300