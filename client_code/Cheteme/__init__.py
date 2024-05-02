from anvil.js.window import jQuery
from anvil import *
from .Memory import Awesome

open_form('Reader.Today')
awesome = Awesome()

def ready(event):
  print('ready')
  print(awesome.get_icon_code('Днес'))
  


if __name__ == "__main__":
  jQuery('document').ready(ready)