from anvil.js.window import jQuery as jQ
import base64

class HtmlElement:
  
  def __init__(self, data: dict = None, css: str or list = None, tag: str = 'dir', text: str = None, ch: bool = True, id: str = None) -> None:

    if data:
      if 'text' in data:
        text = data['text']
      if 'css' in data:
        css = data['css']
      if 'ch' in data:
        ch = data['ch']
      
    self.el = jQ(f'<{tag}>')
    self._text = text
    self._css = css
    self.id = id
    print(self.id)
    
    self.el.addClass(css)
    self.el.text(text)
    self.el.attr('id', self.id)
    self.ch = ch
    
    if self.ch:
      self.el.addClass('ch')

  def css_toggle(self, css):
    self.el.toggleClass(css)
    
  def css_add_class(self, css):
    self.el.addClass(css)

  def css_remove_class(self, css):
    self.el.removeClass(css)
    
  def css_set(self, css):
    self.el.attr('class', css)
    if self.ch:
      self.el.addClass('ch')

  def appendChild(self, child):
    jQ(self.el).append(child.el)

  def visable_toggle(self):
    jQ(self.el).toggle()

  def set_background_image(self, imageData: bytes, ext: str = 'jpeg'):
     image_base64 = base64.b64encode(imageData).decode('utf-8')
     image_url = f'data:image/{ext};base64,{image_base64}'
     jQ(self.el).css('background-image', image_url)
     
  
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
      self.el.css_set(value)


  
  def __str__(self) -> str:
      return self.el.prop('outerHTML')

  def __call__(self) -> object:
      return self.el.prop('outerHTML')


if __name__ == "__main__":
  data = {'text': 'textttt', 'css':'test1'}
  x = HtmlElement(data)
  print(x)
  jQ('body').append(x.el)
  x.css_set('test2')
  x.visable_toggle()
  
 
