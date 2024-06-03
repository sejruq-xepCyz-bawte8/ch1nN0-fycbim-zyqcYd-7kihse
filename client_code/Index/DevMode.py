from . import App

def dev_mode_init():
        print('DEV MODE ON')
        set_constants()

def set_constants():
        print('DEV CONSTANTS ON')
        App.ADULT = True
        App.AUTHOR_ID = 'dev-author-id'
        App.DEVICE_ID = 'dev-device-id'
        App.USER_ID = 'dev-user-id'
        App.IS_AUTHOR = True
        App.IS_DEVICE = True
        App.IS_AUTHOR = True
        App.IS_USER = True
        App.USER_EMAIL = 'dev@chete.me'