from anvil.js.window import jQuery as jQ
from ..Cheteme import awesome

class Icon():
  def __init__(self, name: str = None, bg: str = None) -> None:
    
    if not name : name = awesome.get_icon_code(bg).name
    if not bg : bg = awesome.get_icon_bg(name).bg

    self.bg = bg
    self.name = name
      
    css = f'ch-icon-fa fa-{name}'

    self.el = jQ('<dir>')
    self.el.addClass('ch-icon-container')
    icon = jQ('<i>')
    icon.addClass(css)
    span = jQ('<span>')
    span.text(bg)
    span.addClass('ch-icon-text')
    self.el.append(icon)
    self.el.append(span)
 
  def __str__(self) -> str:
      return self.el.prop('outerHTML')



if __name__ == "__main__":
  i = Icon(bg='Днес')
  i.text = "text"
  print(i)
