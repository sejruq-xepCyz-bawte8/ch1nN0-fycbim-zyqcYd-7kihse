import anvil.server
import hashlib
from time import time


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
        device_id = make_device_id(request_data)
        #anvil.server.cookies.local.set(999, device_id=device_id)
        #anvil.server.session["device_id"] = device_id
    else:
        device_id = suspicious()


    return {'success':True, 'device_id':device_id}





def suspicious():
    pass


def make_device_id(request_data:dict)->str:
    device_id:str = 'new device_id'
    string1 = request_data['ip'] + request_data['session_id'] + str(time())
    hash1 = hash_string(string1)
    midpoint = len(hash1) // 2
    hash1_lhalf = hash1[midpoint:]
    string2 = 'secret' + hash1_lhalf
    hash2 = hash_string(string2)
    hash2_lhalf = hash2[midpoint:]
    return hash2_lhalf + hash1_lhalf


def set_cookie():
    anvil.server.cookies.local.set(36500, device_id="Bob", age=42)


def hash_string(input_string):
    # Convert the string to bytes
    byte_input = input_string.encode('utf-8')
    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the byte data
    sha256_hash.update(byte_input)
    # Get the hexadecimal representation of the hash
    hash_hex = sha256_hash.hexdigest()
    return hash_hex