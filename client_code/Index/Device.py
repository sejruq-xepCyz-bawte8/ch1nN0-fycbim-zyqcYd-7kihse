import anvil.server
from anvil_extras.storage import indexed_db
from anvil.js import window
from anvil.js.window import navigator, screen

device_store = indexed_db.create_store('device')


def has_device() -> bool:
    return True if 'device_id' in device_store else False
    

def init_device() -> bool:
    print('initialising device now ...')
    device_data:dict = {
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
    result = anvil.server.call('init_device', device_data)

    if 'success' in result and 'device_id' in result and result['success']:
        device_store['device_id'] = result['device_id']
        device_store['device_data'] = device_data
        return True
    else:
        return False
    
