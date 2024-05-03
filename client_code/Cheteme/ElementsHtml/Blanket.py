#from anvil.js.window import jQuery as jQ
from .generic import HtmlElement


class Blanket(HtmlElement):
  def __init__(self) -> None:
    super().__init__(tag = 'div', css='ch-blanket')

    self.el.css('z-index', '99999')
    self.el.css('background', 'white')
    self.el.css('width', '100vw')
    self.el.css('height', '100vh')
    self.el.css('position', 'absolute')
    self.el.css('top', '0')
   
    