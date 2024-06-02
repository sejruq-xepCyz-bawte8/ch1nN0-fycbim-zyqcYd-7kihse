import hashlib
from time import time






def make_id(request_data:dict)->str:
    device_id:str = 'new id'
    string1 = request_data['ip'] + request_data['session_id'] + str(time())
    hash1 = hash_string(string1)
    midpoint = len(hash1) // 2
    hash1_lhalf = hash1[midpoint:]
    string2 = 'cheteme' + hash1_lhalf
    hash2 = hash_string(string2)
    hash2_lhalf = hash2[midpoint:]
    return hash2_lhalf + hash1_lhalf



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