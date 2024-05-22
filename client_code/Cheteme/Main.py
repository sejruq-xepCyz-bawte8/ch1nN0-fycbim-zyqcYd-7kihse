from anvil.js.window import jQuery as jQ
from anvil.js.window import document
from anvil import *
import anvil.server
from time import sleep, time

from .ElementsHtml.Navigation import NavigationClass
from .Memory.storage import get_last_open, save_last_open

import anvil.users

from ..APIGate.test_api import test

test()

navigation_list = [
  {'bg':'Днес', 'group':'Reader', 'form':'Today'},
  {'bg':'Творби', 'group':'Reader', 'form':'Works'},
  {'bg':'Автори', 'group':'Reader', 'form':'Authors'},
  {'bg':'Отметки', 'group':'Reader', 'form':'Bookmarks'},
  {'bg':'Вход', 'group':'Reader', 'form':'Login'},
  {'bg':'Настройки', 'group':'Reader', 'form':'Settings'},
  {'bg':'Автор', 'group':'Author', 'form':'Profile'},
  
  {'bg':'Създай', 'group':'Author', 'form':'Editor'},
  {'bg':'Творби', 'group':'Author', 'form':'Works'},
  {'bg':'Стат', 'group':'Author', 'form':'Stat'},
  {'bg':'Профил', 'group':'Author', 'form':'Profile'},
]
navigation_groups = (x['group'] for x in navigation_list)
navigation_forms = (x['form'] for x in navigation_list)
navigation_keys = list(navigation_groups) + list(navigation_forms)

user = anvil.users.get_user()
navigation = NavigationClass(navigation_list=navigation_list)


def update_user_navigation(user):
    navigation = jQ('#navigation')
    
    if user:
        navigation.removeClass('not_user')
        navigation.removeClass('is_author')
        navigation.addClass("is_user")
        if user['is_author']:
            navigation.addClass("is_author")
    else:
        navigation.removeClass('is_user')
        navigation.removeClass('is_author')
        navigation.addClass('not_user')


def navigation_click(proxyobject=None, id=None): #will work on every form
  if id:
    proxyobject = document.getElementById(id)
    classes_click = id.split('.')
  else:
    classes_click = proxyobject.id.split('.')
    
  if not proxyobject and not id:
    proxyobject = document.getElementById('Reader.Today')
  
  try:
        open_form(proxyobject.id) 
  except:
        open_form('Reader.Today')
        proxyobject = document.getElementById('Reader.Today')
  
  
  all_icons = jQ('.ch-icon-container')
  nav = proxyobject.parentNode
  nav.classList.remove(*navigation_keys)
  nav.classList.add(*classes_click)
  all_icons.removeClass('clicked')
  proxyobject.classList.add('clicked')
  save_last_open(proxyobject.id)

def ready(event):
  jQ('body').append(navigation())
  navigation_click(id=get_last_open())
  update_user_navigation(user)
  jQ('#navigation').insertAfter('.anvil-root-container')
  sleep(0.1)
  jQ('html').toggle()
  jQ('#anvil-header').remove()
  jQ('#anvil-badge').remove()
  
  
  
  


 

if __name__ == "__main__":
  jQ('html').toggle()
  jQ('document').ready(ready)
  
