from anvil.js.window import document, location
import anvil.users
from anvil_extras.storage import indexed_db
device_store = indexed_db.create_store('device')
from ..Navigation.NavigationBar import NavigationClass
from ..Database.AwesomeDB import AwesomeClass
from ..Database.GenresDB import GenresClass
from ..Database.EditorDB import EditorClass
from ..Database.ReaderDB import ReaderClass
from ..Database.EngageDB import EngageClass

from .DevMode import dev_mode_init
from .Device import DEVMODE

#Device
DEVICE_ID:str = None
DEVICE_SECRET:str = None

#User
ADULT = None
USER = None
USER_ID:str = None
USER_EMAIL:str = None
IS_USER:bool = None
#Common
AW:AwesomeClass = AwesomeClass()
GENRES:GenresClass = GenresClass()
READER = ReaderClass()
ENGAGE = EngageClass()
#Authors
AUTHOR_ID:str = None
IS_AUTHOR:bool = None
AUTHOR_URI:str = None
AUTHOR_WORKS:dict = None
NAVIGATION:NavigationClass = None
EDITOR:EditorClass = None

def init_app()->bool:
    print('init cheteme app')
    load_js_script('/_/theme/javascript/init_viewport.js')
    load_js_script('https://kit.fontawesome.com/dcfe5f394f.js')
    
    global DEVICE_ID
    global DEVICE_SECRET
    global NAVIGATION

    DEVICE_ID = device_store.get('device_id')
    DEVICE_SECRET = device_store.get('device_id')

    NAVIGATION = NavigationClass()
    
    if not DEVICE_ID or not DEVICE_SECRET:
        return False
    
    USER = anvil.users.get_user()
    
    if USER: init_user()

    if DEVMODE: dev_mode_init()


    return True
 
def load_js_script(src:str) -> None:
    script = document.createElement('script')
    script.src = src
    document.head.appendChild(script)


def init_user()->bool:
    print('init user')
    global USER
    global USER_ID
    global USER_EMAIL
    global IS_USER
    global ADULT
    global IS_AUTHOR

    USER = anvil.users.get_user()
    if USER and not DEVMODE:
        print('is user')
        USER_ID = USER['user_id']
        USER_EMAIL = USER['email']
        IS_USER = bool(USER)
        IS_AUTHOR = USER['is_author']
        ADULT = USER['adult']
    
    if IS_AUTHOR: init_author()

    NAVIGATION.reset()
    return True
    
def init_author():
    print('init author')
    global AUTHOR_ID
    global AUTHOR_URI
    global AUTHOR_WORKS
    global EDITOR

    AUTHOR_DATA = anvil.server.call('get_author_data')
    AUTHOR_ID = AUTHOR_DATA.get('author_id')
    AUTHOR_URI = AUTHOR_DATA.get('author_uri')
    AUTHOR_WORKS = AUTHOR_DATA.get('works')

    
    EDITOR = EditorClass()

    return True
    
    

   
