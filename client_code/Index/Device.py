import anvil.server
from anvil_extras.storage import indexed_db
from anvil.js import window
from anvil.js.window import navigator, screen
from ..API.DeviceIDApi import api_new_device

DEVMODE = True if window.location.hostname is '192.168.0.101' else False
PRODMODE = True if window.location.hostname is 'chete.me' else False

device_store = indexed_db.create_store('device')


def has_device() -> bool:
    if 'device_id' in device_store and 'secret' in device_store:
        return True
    else:
        return False
    

def init_device() -> bool:
    print('initialising new ...')

    
    result = api_new_device()
    if not result:
        return False
    elif not 'success' in result:
        return False
    elif result['success'] == False:
        return False
    elif not 'device_id' in result or not 'secret' in result:
        return False
    else:
        device_store['device_id'] = result['device_id']


    if result and 'success' in result and 'device_id' in result and result['success']:
        device_store['device_id'] = result['device_id']
        device_store['secret'] = result['secret']

        device_store['device_data'] = {
        #navigator
            'hardwareConcurrency':navigator.hardwareConcurrency,
            'maxTouchPoints':navigator.maxTouchPoints,
            'platform':navigator.platform,
            'userAgent':navigator.userAgent,
        #screen
            'colorDepth':screen.colorDepth,
            'height':screen.height,
            'width':screen.width,
            'pixelDepth':screen.pixelDepth,
        #screen_orientation
            'orientation':screen.orientation.type,
    }
        return True
    else:
        if DEVMODE:
            device_store['device_id'] = result['device_id']
            device_store['secret'] = result['secret']
            return True
        return False
    
