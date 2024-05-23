from anvil import *
from Javascript import scriptLoad, scripts, is_touch, screen_info
from JQuery import clean
from _temp.User import update_user
from anvil_extras.hashlib import sha256

device = {}
user = None

print(user)
if __name__ == "__main__":
    #jQ('html').toggle()
    for script in scripts:
        scriptLoad(script)
    clean()
    device['touch'] = is_touch()
    device['screen'] = screen_info()
    user = update_user()
    print(sha256("Hello World!"))
