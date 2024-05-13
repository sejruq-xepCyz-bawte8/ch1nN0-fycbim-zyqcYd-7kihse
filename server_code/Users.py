import anvil.users
import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def sign_up(email, password, code):
  code_row = app_tables.signupcodes.get(code=code)
  if not code_row:
    return {'user':None, 'reason':'Грешен код'}
  if code_row['used'] >= code_row['volume']:
    return {'user':None, 'reason':'Изчерпан код'}
  else:
    try:
      user = anvil.users.signup_with_email(email, password)
      user['is_author'] = code_row['is_author']
      user['code'] = code_row
    except anvil.users.AuthenticationFailed as e:
      return {'user':None, 'reason':f'Неуспешна регистрация - {e}'}
    except anvil.users.PasswordNotAcceptable as e:
      return {'user':None, 'reason':'Неуспешна регистрация - паролата трябва да е поне 8 знака'}
    except anvil.users.UserExists as e:
      return {'user':None, 'reason':'Неуспешна регистрация - има такъв потребител'}
      
    
    if user:
      code_row['used'] += 1
      return {'user':user, 'reason':'Успешна регистрация, активирайте акаунта с изпратения линк в ел. поща', 'is_author': code_row['is_author']}
    else:
      return {'user':user, 'reason':'Неуспешна регистрация'}
      
  

