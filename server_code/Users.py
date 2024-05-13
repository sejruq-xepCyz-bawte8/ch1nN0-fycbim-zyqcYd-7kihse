import anvil.users
import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def sign_up(email, password, code):
  code_row = app_tables.signupcodes.get(code=code)
  if code_row['used'] >= code_row['volume']:
    return {'user':None, 'reason':'Изчерпан код'}
  else:
    try:
      user = anvil.users.signup_with_email(email, password)
    except anvil.users.AuthenticationFailed as e:
      return {'user':None, 'reason':f'Неуспешна регистрация - {e}'}
    
    if user:
      code_row['used'] += 1
      return {'user':user, 'reason':'Успешна регистрация', 'is_author': code_row['is_author']}
    else:
      return {'user':user, 'reason':'Неуспешна регистрация'}
      
  

