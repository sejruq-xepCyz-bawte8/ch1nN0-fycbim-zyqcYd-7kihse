#from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from .Icon import Icon
from anvil import *

navigation = [
  {'bg':'Днес', 'group':'Reader', 'form':'Today'},
  {'bg':'Творби', 'group':'Reader', 'form':'Works'},
  {'bg':'Автори', 'group':'Reader', 'form':'Authors'},
  {'bg':'Отметки', 'group':'Reader', 'form':'Bookmarks'},
  {'bg':'Вход', 'group':'Reader', 'form':'Login'},
  {'bg':'Настройки', 'group':'Reader', 'form':'Settings'},
  {'bg':'Автор', 'group':'Reader', 'form':'Author'},
  
  {'bg':'Създай', 'group':'Author', 'form':'New'},
  {'bg':'Творби', 'group':'Author', 'form':'Works'},
  {'bg':'Стат', 'group':'Author', 'form':'Stat'},
  {'bg':'Профил', 'group':'Author', 'form':'Profile'},
  
]

class NavigationClass(HtmlElement):
  def __init__(self, icons: list = None,) -> None:
    super().__init__(tag = 'div', css='ch-navigation')
    self.clicked = None
    self.current = None
    self.icons = {}
    #jQ('body').append(self.el)
    
    for i in navigation:
      id = f"{i['group']}.{i['form']}"
      css = f"{i['group']} {i['form']}"
      icon = Icon(bg=i['bg'], id = id)
      icon.css_add_class(css)
      icon.el.click(self.click)
      self.icons[id] = icon
      self.appendChild(icon)

  def click(self, event):
    self.el.children().removeClass('test')
    id = event.currentTarget.id
    try:
      open_form(id)
    except:
      open_form('Reader.Today')
  
    nav_css = id.split('.')
    self.css_remove_class(self.current)
    self.css_add_class(nav_css)
    self.current = nav_css
    self.icons[id].css_add_class('test')
    
    
if __name__ == "__main__":
  i = Navigation()
  
  



