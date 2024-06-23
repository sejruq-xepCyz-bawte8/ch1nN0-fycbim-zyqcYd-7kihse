from anvil_extras.hashlib import sha256


def hash_strings(*args)->str:
    input_string = ''.join(args)
    hash_hex = sha256(input_string)

    return hash_hex