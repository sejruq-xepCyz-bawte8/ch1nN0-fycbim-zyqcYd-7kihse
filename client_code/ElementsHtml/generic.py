from anvil.js.window import jQuery as jQ

class HtmlElement:
  def __init__(self, css = None, tag: str = "div", text: str = "", cheteme: bool = True) -> None:
    self.el = jQ(f'<{tag}>')
    self._text = text
    self.css = css

    
    self.el.addClass(css)
    self.el.text(text)
  
  def add_cssclass(self):
    pass

  def appendChild(self, child):
    jQ(self.el).append(child.el)
    
  @property
  def text(self):
      return self._text

  @text.setter
  def text(self, value):
      self._text = value
      self.el.text(text)
  
  def __str__(self) -> str:
      return self.el.prop('outerHTML')

  def __call__(self) -> object:
      return self.el


if __name__ == "__main__":
  data = {'text': 'textttt'}
  x = HtmlElement(text="test")
  print(x)
