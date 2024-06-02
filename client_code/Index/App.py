from anvil.js.window import document
from anvil_extras.storage import indexed_db
device_store = indexed_db.create_store('device')
from ..Navigation.NavigationBar import NavigationClass
from ..Database.AwesomeDB import AwesomeClass

USER = None
USER_ID:str = None
USER_EMAIL:str = None
IS_USER:bool = None
DEVICE_ID:str = None
AUTHOR_ID:str = None
IS_AUTHOR:bool = None


NAVIGATION:NavigationClass = None
AW:AwesomeClass = None

def init_app()->bool:
    load_js_script('https://kit.fontawesome.com/dcfe5f394f.js')
    global NAVIGATION
    global DEVICE_ID
    global AW
    DEVICE_ID = device_store['device_id']
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

    USER = user if user else None
    USER_ID = user['user_id'] if user else None
    USER_EMAIL = user['email'] if user else None
    IS_USER = bool(user) if user else None
    AUTHOR_ID = user['author_id'] if 'author_id' in user and user['author_id'] else None
    IS_AUTHOR = bool(user['author_id']) if 'author_id' in user and user['author_id'] else None

    NAVIGATION.reset()

    return True
