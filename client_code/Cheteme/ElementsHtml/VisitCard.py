from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from .Icon import Icon
from anvil import *
from ..Memory import genres



class VisitCardClass(HtmlElement):
  def __init__(self, data: dict) -> None:
    if not 'id' in data: data['id'] = 'testid'
    
    super().__init__(tag = 'div', css='ch-visitcard', id=data['id'])
    self.data = data
    #self.el.attr('onclick', "authorClick(this, event)")

    self.header = HtmlElement(tag='dir', css='ch-visitcard-header')
    self.title = HtmlElement(tag='dir', css='ch-visitcard-title', text=data['title'])
    self.icons = HtmlElement(tag='div', css='ch-visitcard-icons')

    
    if 'g' in data:
      for g in data['g']:
        aw = genres.get_one(key="gid", value=g)
        if aw:
          icon = Icon(bg=aw['bg'], id=g)
          self.icons.appendChild(icon)
    
    self.appendChild(self.header)
    self.appendChild(self.title)
    self.appendChild(self.icons)


  def click(self, event):
    print(event)
  
   
    
if __name__ == "__main__":
  pass
  
  



