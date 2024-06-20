from anvil.js import window


CRYPTO = window.crypto

def hash_strings(*args)->str:
    input_string = ''.join(args)
    
    dataBuffer = input_string.encode('utf-8')

    hashBuffer = window.crypto.subtle.digest('SHA-256', dataBuffer)
    byteArray = window.Uint8Array(hashBuffer)
    print(byteArray)
    #hash_hex = ''.join(format(byte, '02x') for byte in hash_array)
    #sha256_hash = hashlib.sha256()
    #sha256_hash.update(byte_input)
    #hash_hex = sha256_hash.hexdigest()
    #return hash_hex