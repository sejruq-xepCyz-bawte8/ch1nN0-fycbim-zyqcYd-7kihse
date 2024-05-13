from anvil.js.window import jQuery as jQ
from anvil.js.window import document
from anvil import *
from time import sleep, time

from .ElementsHtml.Navigation import NavigationClass
from .ElementsHtml.Blanket import Blanket

import anvil.users

user = None
navigation = None

navigation_list = [
  {'bg':'Днес', 'group':'Reader', 'form':'Today'},
  {'bg':'Творби', 'group':'Reader', 'form':'Works'},
  {'bg':'Автори', 'group':'Reader', 'form':'Authors'},
  {'bg':'Отметки', 'group':'Reader', 'form':'Bookmarks'},
  {'bg':'Вход', 'group':'Reader', 'form':'Login'},
  {'bg':'Настройки', 'group':'Reader', 'form':'Settings'},
  {'bg':'Автор', 'group':'Author', 'form':'Profile'},
  
  {'bg':'Създай', 'group':'Author', 'form':'New'},
  {'bg':'Творби', 'group':'Author', 'form':'Works'},
  {'bg':'Стат', 'group':'Author', 'form':'Stat'},
  {'bg':'Профил', 'group':'Author', 'form':'Profile'},
]
navigation_groups = (x['group'] for x in navigation_list)
navigation_forms = (x['form'] for x in navigation_list)
navigation_keys = list(navigation_groups) + list(navigation_forms)



def ready(event):
  global navigation
  print("Ready")
  navigation = NavigationClass(navigation_list=navigation_list)
  update_user()
  
  today = document.getElementById("Reader.Today")
  
  navigation_click(today)

  
  #sleep(0.5)
  #blanket.toggle()
  
  
def navigation_click(proxyobject): #will work on every form
  classes_click = proxyobject.id.split('.')
  proxyobject.parentNode.classList.remove(*navigation_keys)
  proxyobject.parentNode.classList.add(*classes_click)
  jQ('.ch-icon-container').removeClass('clicked')
  proxyobject.classList.add('clicked')
  try:
        open_form(proxyobject.id)
  except:
        open_form('Reader.Today')

 
def update_user():
    user = anvil.users.get_user()
    if user:
        navigation.css_remove_class('not_user')
        navigation.css_remove_class('is_author')
        navigation.css_add_class("is_user")
        if user.is_author:
            navigation.css_add_class("is_author")
    else:
        navigation.css_remove_class('is_user')
        navigation.css_remove_class('is_author')
        navigation.css_add_class('not_user')
    
        



if __name__ == "__main__":
  print("Main start")
  #blanket = Blanket()()
  #jQ('body').append(blanket)
  jQ('document').ready(ready)
  
