from anvil.js.window import jQuery as jQ
from anvil import *
from time import sleep, time

from .ElementsHtml.Navigation import NavigationClass
from .ElementsHtml.Blanket import Blanket



def ready(event):
  navigation = NavigationClass()()
  open_form('Reader.Today')
  jQ('body').append(navigation)
  sleep(0.5)
  blanket.toggle()
  
  
  
  


if __name__ == "__main__":
  blanket = Blanket()()
  jQ('body').append(blanket)
  jQ('document').ready(ready)
  
  
  