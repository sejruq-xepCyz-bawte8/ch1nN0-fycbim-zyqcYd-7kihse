from anvil.js.window import jQuery as jQ

class HtmlElement:
  def __init__(self, data: dict = None, css: str or list = None, tag: str = 'dir', text: str = None, cheteme: bool = True) -> None:
    if data:
      if 'text' in data:
        text = data['text']
      if 'css' in data:
        css = data['css']


    self.el = jQ(f'<{tag}>')
    self._text = text
    self._css = css

    self.el.addClass(css)
    self.el.text(text)

    
  def add_css(self, css):
    self.el.addClass(css)
    
  def set_css(self, css):
    self.el.attr('class', css)

  def appendChild(self, child):
    jQ(self.el).append(child.el)
    
  @property
  def text(self):
      return self._text

  @text.setter
  def text(self, value):
      self._text = value
      self.el.text(value)

  @property
  def css(self):
      return self._css

  @css.setter
  def css(self, value):
      self._css = value
      self.el.addClass(value)


  
  def __str__(self) -> str:
      return self.el.prop('outerHTML')

  def __call__(self) -> object:
      return self.el


if __name__ == "__main__":
  data = {'text': 'textttt', 'css':'test'}
  x = HtmlElement(data)
  print(x)
  jQ('body').append(x.el)
 
