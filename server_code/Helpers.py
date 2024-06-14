import hashlib
from time import time
from Suspicious import log_suspicious
import re
import anvil.server

def is_valid_uri(uri:str)->bool:
    pattern = re.compile(r'^[a-zA-Z0-9._~%-]+$')
    if pattern.match(uri):
        return True
    else:
        status(f'Невалиден линк: {uri}')
        return False

def has_keys(target:dict, keys:list)->bool:
    for key in keys:
        value = target.get(key)
        if not value:
            status(f'Непълни метаданни - {key}')
            return False
    return True


def is_user_author(user, client)->bool:
    user_id = user.get('user_id')
    is_author = user.get('is_author')
    if not user_id or not is_author:
        task = log_suspicious(cheteme='publish work', client=client)
        status('Невалиден потребител/автор')
        return False
    else:
        return True
    

def hash_strings(*args)->str:
    input_string = ''.join(args)
    byte_input = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(byte_input)
    hash_hex = sha256_hash.hexdigest()
    return hash_hex

def has_record(target, record_hash:str):
   return True if target.get(hash=record_hash) else False

def status(message):
   anvil.server.task_state = message

def fail(message):
   anvil.server.task_state = message
   return False