import anvil.server
from .IDGenerator import make_id


@anvil.server.callable
def init_device(device_data):
    try:
        location = anvil.server.context.client.location.country_code
    except:
        location = None
    request_data:dict = {
        'ip':anvil.server.context.client.ip,
        'session_id':anvil.server.session.session_id,
        'type':anvil.server.context.remote_caller.type,
        'location': location,
    }
    
    device_id_cookie = anvil.server.cookies.local.get("device_id", None)
    device_id_session = anvil.server.session.get("device_id", None)

    if not device_id_cookie and not device_id_session and request_data['type']=='browser':
        device_id = make_id(request_data)
        #anvil.server.cookies.local.set(999, device_id=device_id)
        #anvil.server.session["device_id"] = device_id
    else:
        device_id = suspicious()

    return {'success':True, 'device_id':device_id}


def suspicious():
    pass

def set_cookie():
    anvil.server.cookies.local.set(36500, device_id="Bob", age=42)


