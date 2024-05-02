from anvil.js.window import jQuery
from anvil import *

class CNAV:
  def __init__(self):
    self.navigation = jQuery('<div>nav</div>')
    

navigation = [
  {'bg':'Днес', 'group':'Reader', 'form':'Today'},
  {'bg':'Творби', 'group':'Reader', 'form':'Works'}
]

template = "<div><i>{title}</i></div>"


open_form('Reader.Today')
def append(*data):
  jQuery('body').append(data[0])
 

jQuery.get('_/theme/navigation.html', append)

nav = jQuery('<div>nav</div>')
jQuery('body').append(nav)

def test(event):
  print(event.target.innerText)
  open_form(f'Reader.{event.target.innerText}')

for n in navigation:
  link_html = template.format(title=n['title'])
  link = jQuery(link_html)
  link.on('click', test)
  nav.append(link)
  


