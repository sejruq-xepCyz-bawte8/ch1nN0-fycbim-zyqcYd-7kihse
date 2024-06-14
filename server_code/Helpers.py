import hashlib
from time import time
import re
import anvil.server
from anvil.tables import app_tables
from datetime import datetime

def is_valid_uri(uri:str)->bool:
    pattern = re.compile(r'^[a-zA-Z0-9._~%-]+$')
    if pattern.match(uri):
        return True
    else:
        status(f'Невалиден линк: {uri}')
        return False

def has_keys(target:dict, keys:list)->bool:
    for key in keys:
        if not key in target:
            status(f'Непълни метаданни - {key}')
            return False
    return True


def is_user_author(user, client)->bool:
    user_id = user.get('user_id')
    is_author = user.get('is_author')
    if user_id and is_author:
        return True
    elif not user_id or not is_author:
        log_suspicious(cheteme='publish work', client=client)
        status('Невалиден потребител/автор')
        return False
    else:
        return False
    

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
   anvil.server.task_state['message'] = message
   

def fail(message):
   anvil.server.task_state['message'] = message
   return False


def log_suspicious(cheteme:str, client):
     app_tables.suspicious.add_row(datetime=datetime.datetime.now(),
                                      type=client.type,
                                      ip=client.ip,
                                      location=client.location,
                                      cheteme=cheteme)