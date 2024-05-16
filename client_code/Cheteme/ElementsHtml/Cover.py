#from anvil.js.window import jQuery as jQ
from .generic import HtmlElement
from .Icon import Icon
from anvil import *
import anvil.server



class CoverClass(HtmlElement):
  def __init__(self, data: dict) -> None:
    if not 'id' in data: data['id'] = 'testid'
    if not 'cover' in data: data['cover'] = None
    super().__init__(tag = 'div', css='ch-cover', id=data['id'])
    self.data = data

    if self.data['cover']:
       print('has cover')
       self.set_background_image(self.data['cover'])
    self.title = HtmlElement(tag='dir', css='ch-cover-title', text=data['title'])
    self.icons = HtmlElement(tag='div', css='ch-cover-icons')
    self.cover_mask = HtmlElement(tag='div', css='ch-cover-mask')
    
    if 'genre' in data:
      if data['genre']:
         self.icons.appendChild(Icon(bg=data['genre']))
         if 'subgenre' in data:
            if data['subgenre']:
               self.icons.appendChild(Icon(bg=data['subgenre']))
    
    
    if 'keywords' in data:
      i = 1
      for k in data['keywords']:
         if i <= 3:
               self.icons.appendChild(Icon(bg=k))
         i += 1
  
    if 'cover' in data:
       self.set_background_image(data['cover'])
    if 'color' in data:
       self.el.css('color', data['color'])
    if 'background' in data:
       self.el.css('background-color', data['background'])
    if 'font' in data:
       self.title.el.css('font-family', data['font'])
    if 'cover_mask' in data:
       mask = int(data['cover_mask']) / 100
       hex_shadow = data['shadow'].lstrip('#')
       rgb = tuple(int(hex_shadow[i:i+2], 16) for i in (0, 2, 4))
       #mask_color = f'fill 0 linear-gradient(to top, rgba({rgb[0]},{rgb[1]},{rgb[2]},{mask}) 0%, rgba({rgb[0]},{rgb[1]},{rgb[2]},0) 100%)'
       
       mask_color = f'linear-gradient(to top, rgba({rgb[0]},{rgb[1]},{rgb[2]},{mask}) 0%, rgba({rgb[0]},{rgb[1]},{rgb[2]}, 0) 100%)'
       self.cover_mask.el.css('background-image', mask_color)

       #self.el.css('border-image', mask_color)


    self.cover_mask.appendChild(self.title)
    self.cover_mask.appendChild(self.icons)
    #self.appendChild(self.title)
    #self.appendChild(self.icons)
    self.appendChild(self.cover_mask)


  def click(self, event):
    print(event)
  
    
    
if __name__ == "__main__":
  i = CoverClass()
  print(i())
  
  



