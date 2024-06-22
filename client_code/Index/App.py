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

GOOGLEFONTS = 'https://fonts.googleapis.com/css2?family=Alumni+Sans+Pinstripe:ital@0;1&family=Caveat:wght@400..700&family=Comfortaa:wght@300..700&family=Cormorant+Infant:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Days+One&family=El+Messiri:wght@400..700&family=Exo+2:ital,wght@0,100..900;1,100..900&family=Gabriela&family=Great+Vibes&family=Lobster&family=Noto+Serif:ital,wght@0,100..900;1,100..900&family=Orelega+One&family=Oswald:wght@200..700&family=Pacifico&family=Pattaya&family=Playfair+Display+SC:ital,wght@0,400;0,700;0,900;1,400;1,700;1,900&family=Prosto+One&family=Rampart+One&family=Roboto+Serif:ital,opsz,wght@0,8..144,100..900;1,8..144,100..900&family=Rubik+Mono+One&family=Rubik+Moonrocks&family=Ruslan+Display&family=Russo+One&family=Seymour+One&family=Sofia+Sans+Condensed:ital,wght@0,1..1000;1,1..1000&family=Sofia+Sans+Extra+Condensed:ital,wght@0,1..1000;1,1..1000&family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&family=Tektur:wght@400..900&family=Unbounded:wght@200..900&family=Vollkorn:ital,wght@0,400..900;1,400..900&family=Yanone+Kaffeesatz:wght@200..700&family=Yeseva+One&display=swap'


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
    load_js_links(href='https://fonts.googleapis.com', rel='preconnect')
    load_js_links(href='https://fonts.gstatic.com', rel='preconnect', crossorigin=True)
    load_js_links(href=GOOGLEFONTS, rel='stylesheet')
    
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

def load_js_links(href:str, rel:str = None, crossorigin:bool = False) -> None:
    link = document.createElement('link')
    link.href = href
    if rel: link.rel = rel
    if crossorigin: link.crossOrigin = 'anonymous'
    document.head.appendChild(link)


#<link rel="preconnect" href="https://fonts.googleapis.com">
#<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#<link href="https://fonts.googleapis.com/css2?family=Alumni+Sans+Pinstripe:ital@0;1&family=Caveat:wght@400..700&family=Comfortaa:wght@300..700&family=Cormorant+Infant:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Days+One&family=El+Messiri:wght@400..700&family=Exo+2:ital,wght@0,100..900;1,100..900&family=Gabriela&family=Great+Vibes&family=Lobster&family=Noto+Serif:ital,wght@0,100..900;1,100..900&family=Orelega+One&family=Oswald:wght@200..700&family=Pacifico&family=Pattaya&family=Playfair+Display+SC:ital,wght@0,400;0,700;0,900;1,400;1,700;1,900&family=Prosto+One&family=Rampart+One&family=Roboto+Serif:ital,opsz,wght@0,8..144,100..900;1,8..144,100..900&family=Rubik+Mono+One&family=Rubik+Moonrocks&family=Ruslan+Display&family=Russo+One&family=Seymour+One&family=Sofia+Sans+Condensed:ital,wght@0,1..1000;1,1..1000&family=Sofia+Sans+Extra+Condensed:ital,wght@0,1..1000;1,1..1000&family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&family=Tektur:wght@400..900&family=Unbounded:wght@200..900&family=Vollkorn:ital,wght@0,400..900;1,400..900&family=Yanone+Kaffeesatz:wght@200..700&family=Yeseva+One&display=swap" rel="stylesheet">

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
    
    

   
