from anvil.js.window import document
import anvil.users
from anvil_extras.storage import indexed_db
device_store = indexed_db.create_store('device')
from ..Navigation.NavigationBar import NavigationClass
from ..Database.AwesomeDB import AwesomeClass

ADULT = None
USER = None
USER_ID:str = None
USER_EMAIL:str = None
IS_USER:bool = None
IS_DEVICE:bool = None
DEVICE_ID:str = None
AUTHOR_ID:str = None
IS_AUTHOR:bool = None


NAVIGATION:NavigationClass = None
AW:AwesomeClass = None

def init_app()->bool:
    load_js_script('https://kit.fontawesome.com/dcfe5f394f.js')
    global NAVIGATION
    global DEVICE_ID
    global IS_DEVICE
    global AW
    DEVICE_ID = device_store['device_id']
    IS_DEVICE = bool(DEVICE_ID)
    AW = AwesomeClass() # beff others
    NAVIGATION = NavigationClass()
    return True

def load_js_script(src:str) -> None:
    script = document.createElement('script')
    script.src = src
    document.head.appendChild(script)

def init_user(user)->bool:
    global USER
    global USER_ID
    global USER_EMAIL
    global IS_USER
    global AUTHOR_ID
    global IS_AUTHOR
    global ADULT
  
    USER = anvil.users.get_user()
    USER_ID = USER['user_id'] if USER else None
    USER_EMAIL = USER['email'] if USER else None
    IS_USER = bool(USER)
    AUTHOR_ID = USER['author_id'] if USER and 'author_id' in USER else None
    ADULT = USER['adult'] if USER and 'adult' in USER else None
    IS_AUTHOR = USER['is_author'] if USER and 'is_author' in USER else None
    
    NAVIGATION.reset()

    return True
