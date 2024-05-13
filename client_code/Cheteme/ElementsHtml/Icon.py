import anvil.server
from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from ..Memory import awesome


class Icon(HtmlElement):
  def __init__(self, name: str = None, bg: str = None, style='light', id: str = None) -> None:
    super().__init__(tag = 'span', css='ch-icon-container', id = id)
  
    if not name :
      name_search = awesome.get_icon_code(bg.lower())
      if name_search:
        name = name_search
      else:
        name = 'icons'
    if not bg :
      bg_search = awesome.get_icon_bg(name)
      if bg_search:
        bg = bg_search.bg
      else:
        bg = 'Икона'

    self._name = name
    self._bg = bg
    self._style = style
    
    self.icon = HtmlElement(tag='i', css='ch-icon-fa')
    self.css_icon(self.name)
    
    self.span = HtmlElement(tag='span', css='ch-icon-text')
    self.span.text = bg
    


    self.appendChild(self.icon)
    self.appendChild(self.span)

  
  def css_icon(self, name):
    css = f'fa-{self.style} fa-{self.name}'
    self.icon.css_add_class(css)

  def change_icon(self, old_name, new_name):
    self.icon.css_remove_class(f'fa-{old_name}')
    self.icon.css_add_class(f'fa-{new_name}')

  
  @property
  def bg(self):
      return self._bg
  @bg.setter
  def bg(self, value):
      old = self.name
      self._bg = value
      self.name = awesome.get_icon_code(value).name
      self.change_icon(old, self.name)
      self.span.text = value
    
      
  @property
  def name(self):
      return self._name
  @name.setter
  def name(self, value):
      old = self.name
      self._name = value
      self.change_icon(old, self.name)

  @property
  def style(self):
      return self._style
  @style.setter
  def style(self, value):
      old = self.style
      self._style = value
      self.change_icon(old, self.style)

if __name__ == "__main__":
  i = Icon(bg='Днес')
  
  print(i)
  jQ('body').append(i())
  i.css_add_class('test')
  i.style = 'duotone'
  print(i)
