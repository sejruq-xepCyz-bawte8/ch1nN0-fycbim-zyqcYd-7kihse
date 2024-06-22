from . import App
from ..Database.EditorDB import EditorClass

def dev_mode_init():
        print('DEV MODE ON')
        set_constants()

def set_constants():
        print('DEV CONSTANTS ON')
        App.ADULT = True
        App.AUTHOR_ID = 'a40e72f616758859f8610fd76761f93fabc4e2c75d75fb43e299fbd8cda2cddb' #beach
        App.USER_ID = 'dev-user-id'
        App.IS_AUTHOR = True
        App.IS_USER = True
        App.USER_EMAIL = 'dev@chete.me'
        App.EDITOR = EditorClass()
   