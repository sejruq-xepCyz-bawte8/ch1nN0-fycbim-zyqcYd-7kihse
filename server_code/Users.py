import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import anvil.server
from .IDGenerator import make_id


def init_user(device_data=None):
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
    
    user_id_cookie = anvil.server.cookies.local.get("user_id", None)
    user_id_session = anvil.server.session.get("user_id", None)

    if not user_id_cookie and not user_id_session and request_data['type']=='browser':
        user_id = make_id(request_data)
        return {'success':True, 'user_id':user_id}
    else:
        user_id = suspicious(request_data)
        return {'success':False, 'message':'Unknown :)'}


def suspicious(request_data):
    print('suspicious sign up', request_data)


def set_cookie():
    anvil.server.cookies.local.set(36500, device_id="Bob", age=42)


def check_code(code):
    code_row = app_tables.signupcodes.get(code=code)
    if not code_row:
        return {'success':False, 'message':'Грешен код'}
    elif code_row['used'] >= code_row['volume']:
        return {'success':False, 'message':'Изчерпан код'}
    else:
        return {'success':True, 'code_row':code_row}

@anvil.server.callable
def sign_up(email:str, password:str, code:str, adult:bool):
    valid_code = check_code(code)
    if not valid_code['success']: return valid_code
    valid_id = init_user()
    if not valid_id['success']: return valid_id
    
    code_row = valid_code['code_row']
    user_id = valid_id['user_id']
    try:
      user = anvil.users.signup_with_email(email, password)
      user['is_author'] = code_row['is_author']
      user['code'] = code
      user['user_id'] = user_id
      user['adult'] = adult

    except anvil.users.AuthenticationFailed as e:
      return {'success':False, 'user':None, 'message':f'Неуспешна регистрация - {e}'}
    except anvil.users.PasswordNotAcceptable as e:
      return {'success':False, 'user':None, 'message':'Неуспешна регистрация - паролата трябва да е поне 8 знака'}
    except anvil.users.UserExists as e:
      return {'success':False, 'user':None, 'message':'Неуспешна регистрация - има такъв потребител'}
      
    if user:
      code_row['used'] += 1
      return {'success':True, 'user':user, 'message':'Успешна регистрация, активирайте акаунта с изпратения линк в ел. поща', 'is_author': code_row['is_author']}
    else:
      return {'success':False, 'user':None, 'message':'Неуспешна регистрация'}
      