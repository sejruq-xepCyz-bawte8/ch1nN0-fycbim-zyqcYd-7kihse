import anvil.users
from anvil.js.window import document

class HtmlElement:
  def __init__(self, classlist: list, tag: str = "div", text: str = "", cheteme: bool = True) -> None:
    self.el = document.createElement(tag)
    self._text = text
    self.cssclasses = classlist
  
  def add_cssclass(self):
    pass
    
  @property
  def text(self):
      return self._text

  @text.setter
  def text(self, value):
      self._text = value
      self.el.innerText = value
  
  def __str__(self) -> str:
      return f'{self.el.outerHTML}'

  def __call__(self) -> object:
      return self.el


if __name__ == "__main__":
  data = {'text': 'textttt'}
  x = HtmlElement(text="test")
  print(x)