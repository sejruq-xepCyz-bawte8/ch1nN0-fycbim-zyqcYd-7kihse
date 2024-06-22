import anvil.server
from anvil_extras.storage import indexed_db
from anvil.js import window
from anvil.js.window import navigator, screen
from ..API.DeviceIDApi import api_new_device

DEVMODE = True if window.location.hostname is '192.168.0.101' else False

device_store = indexed_db.create_store('device')


def has_device() -> bool:
    if 'device_id' in device_store and 'secret' in device_store:
        return True
    else:
        return False
    

def init_device() -> bool:
    print('initialising new device ...')
    result = api_new_device()
    success = result.get('success')
    
    if success:
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
        print('cannot initialise new device ...')
        return False
    
