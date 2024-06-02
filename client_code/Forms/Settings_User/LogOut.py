from ...Index.App import init_user
import anvil.users

def logout_user(*args, **kwargs):
      user =anvil.users.logout()
      if not user:
          init = init_user()
      if init:
          result = {'success':True, 'message':'Успешен изход'}
      else:
            result = {'success':False, 'message':'Неуспешен изход'}

      return result
