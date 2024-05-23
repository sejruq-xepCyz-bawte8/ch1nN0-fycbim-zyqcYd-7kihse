from anvil_extras.storage import local_storage
from anvil_extras.hashlib import sha1
from anvil_extras.uuid import uuid4
from time import time
from anvil.js import window
from anvil.js.window import document
from anvil.js.window import navigator



def first_load():
    device = {}
    device_screen = {}
    device['device_id'] = generate_devide_id()
    device_screen.update(is_touch())
    device_screen.update(screen_info())
    device['screen'] = device_screen
    local_storage['device'] = device
    return device

def generate_devide_id():
    string = str(uuid4()) + str(time())
    device_id = sha1(string)
    return device_id

def is_touch(addclass:bool = True):
    if 'ontouchstart' in window:
        result = 'is_touch'
    elif 'maxTouchPoints' in navigator:
        if navigator.maxTouchPoints > 0 :
            result = 'is_touch'
    elif 'msMaxTouchPoints' in navigator:
        if navigator.msMaxTouchPoints > 0 :
            result = 'is_touch'
    result = 'not_touch'
    return {'touch':result}

def screen_info(addclass:bool = True):
    width = window.screen.width
    height = window.screen.height
    if width > height:
        orientation = "portrait_screen"
    else:
        orientation = "landscape_screen"
    if width < 400:
        size = 'small_screen'
    elif width < 600:
        size = 'medium_screen'
    elif width < 800:
        size = 'big_screen'
    else:
        size = 'large_screen'
    return {'width':width,'heigth':height,'orientation':orientation,'size':size}