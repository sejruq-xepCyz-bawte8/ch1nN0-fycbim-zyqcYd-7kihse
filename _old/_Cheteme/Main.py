from anvil.js.window import jQuery as jQ
from anvil.js.window import document
from anvil import *
import anvil.server
from time import sleep, time

from .ElementsHtml.Navigation import NavigationClass
from .Memory.storage import get_last_open, save_last_open

import anvil.users





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


def navigation_click(element_id): #will work on every form
  navigation_element = jQ('#navigation')
  print(element_id)
  try:
        open_form(element_id)  
  except:
        open_form('Reader.Today')
        element_id = 'Reader.Today'
  
  classes_nav = element_id.replace('.', ' ')
  element_clicked = jQ('#Reader.Today')

  navigation_element.children().removeClass('clicked')
  navigation_element.removeClass(navigation_keys)
  navigation_element.addClass(classes_nav)
  print(element_id, element_clicked, element_clicked.attr('id'))
  print(navigation_element, navigation_element.attr('id'))

  element_clicked.addClass('clicked')
  element_clicked.css('background-color', 'blue')
  

  save_last_open(element_id)

def ready(event):
  jQ('body').append(navigation())
  navigation_click(get_last_open())
  update_user_navigation(user)
  jQ('#navigation').insertAfter('.anvil-root-container')
  sleep(0.1)
  jQ('html').toggle()
  jQ('#anvil-header').remove()
  jQ('#anvil-badge').remove()
  
  
  
  


 

if __name__ == "__main__":
  jQ('html').toggle()
  jQ('document').ready(ready)
  
