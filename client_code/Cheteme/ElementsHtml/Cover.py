#from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from .Icon import Icon
from anvil import *



class CoverClass(HtmlElement):
  def __init__(self, data: dict) -> None:
    
    super().__init__(tag = 'div', css='ch-cover', id=dict['id'])
    self.data = data
    self.title = HtmlElement(tag='dir', css='ch-cover-title', text=data['title'])
    self.icons = HtmlElement(tag='div', css='ch-cover-icons')
    
    self.icons.appendChild(Icon(bg=data['genre']))
    self.icons.appendChild(Icon(bg=data['subgenre']))
    i = 0
    
    keywords = data['keywords'].split(",")
    
    for k in keywords:
        if i <= 3:
            self.icons.appendChild(Icon(bg=k))
        i += 1
  
    if data['cover']:
       self.set_background_image(data['cover'])
    
    self.appendChild(self.title)
    self.appendChild(self.icons)

  def click(self, event):
    print(event)
  
    
    
if __name__ == "__main__":
  i = CoverClass()
  print(i())
  
  



