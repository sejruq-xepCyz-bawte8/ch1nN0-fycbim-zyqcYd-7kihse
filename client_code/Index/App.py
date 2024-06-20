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

from .Device import DEVMODE, PRODMODE

ADULT = None
USER = None
USER_ID:str = None
USER_EMAIL:str = None
IS_USER:bool = None
IS_DEVICE:bool = None
DEVICE_ID:str = None
SECRET:str = None
AUTHOR_ID:str = None
IS_AUTHOR:bool = None


NAVIGATION:NavigationClass = None
AW:AwesomeClass = AwesomeClass()
GENRES:GenresClass = GenresClass()

EDITOR:EditorClass = None
READER:ReaderClass = None
ENGAGE:EngageClass = None

def init_app()->bool:
    load_js_script('/_/theme/javascript/init_viewport.js')
    load_js_script('https://kit.fontawesome.com/dcfe5f394f.js')

    global NAVIGATION
    global DEVICE_ID
    global SECRET
    global IS_DEVICE
    global AW
    DEVICE_ID = device_store['device_id']
    SECRET = device_store['secret']
    IS_DEVICE = bool(DEVICE_ID)
    

    global USER
    global USER_ID
    global USER_EMAIL
    global IS_USER
    global AUTHOR_ID
    global IS_AUTHOR
    global ADULT
    global EDITOR
    global READER
    global ENGAGE
  
    USER = anvil.users.get_user()
    USER_ID = USER['user_id'] if USER else None
    USER_EMAIL = USER['email'] if USER else None
    IS_USER = bool(USER)
    AUTHOR_ID = USER['author_id'] if USER and 'author_id' in USER else None
    ADULT = USER['adult'] if USER and 'adult' in USER else None
    IS_AUTHOR = USER['is_author'] if USER and 'is_author' in USER else None

    #AW = AwesomeClass() # beff others
    

    if DEVMODE:dev_mode_init()

    EDITOR = EditorClass() if IS_AUTHOR else None
    
    NAVIGATION = NavigationClass()
    READER = ReaderClass()
    ENGAGE = EngageClass()
    return True

def load_js_script(src:str) -> None:
    script = document.createElement('script')
    script.src = src
    document.head.appendChild(script)

def init_user()->bool:
    global USER
    global USER_ID
    global USER_EMAIL
    global IS_USER
    global AUTHOR_ID
    global IS_AUTHOR
    global ADULT
    global EDITOR
  
    USER = anvil.users.get_user()
    USER_ID = USER['user_id'] if USER else None
    USER_EMAIL = USER['email'] if USER else None
    IS_USER = bool(USER)
    IS_AUTHOR = USER['is_author'] if USER and 'is_author' in USER else None
    if IS_AUTHOR and USER['author_id']:
        AUTHOR_ID = USER['author_id']
    else:
        AUTHOR_ID = anvil.server.call('get_author_id')
    
    ADULT = USER['adult'] if USER and 'adult' in USER else None
    
    
    EDITOR = EditorClass() if IS_AUTHOR else None
    NAVIGATION.reset()

    return True
