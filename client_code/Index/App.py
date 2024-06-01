from anvil.js.window import document
from anvil_extras.storage import indexed_db
device_store = indexed_db.create_store('device')
from ..Navigation.NavigationBar import NavigationClass
from ..Database.AwesomeDB import AwesomeClass

DEVICE_ID:str = None
USER_ID:str = None
AUTHOR_ID:str = None
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