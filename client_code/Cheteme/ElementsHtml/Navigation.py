from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from .Icon import Icon
from anvil import *



class NavigationClass(HtmlElement):
  def __init__(self, icons: list = None, navigation_list: list = None) -> None:
    super().__init__(tag = 'div', css='ch-navigation')
    self.clicked = None
    self.current = None
    self.icons = {}
    jQ('body').append(self.el)
    
    for i in navigation_list:
      id = f"{i['group']}.{i['form']}"
      css = f"{i['group']} {i['form']}"
      icon = Icon(bg=i['bg'], id = id)
      icon.css_add_class(css)
      icon.el.attr('onclick', "navClick(this, event)")
      self.icons[id] = icon
      self.appendChild(icon)
      


    
if __name__ == "__main__":
  i = Navigation()
  
  



