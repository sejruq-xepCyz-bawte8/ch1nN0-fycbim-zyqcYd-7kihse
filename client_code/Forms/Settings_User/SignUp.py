import anvil.server
from ...Index.App import init_user


def sign_up_new_user(email:str, password:str, code:str, adult:bool):
      try:
        result = anvil.server.call('sign_up', email=email, password=password, code=code, adult=adult)
        if not result['success'] :
          return result
        else:
          user = result['user'] if 'user' in result else None
        if user:
            init = init_user()
        if init:
            result = {'success':True, 'message':f'Успешена регистрация: {user["email"]}, активирайте акаунта с изпратения линк.'}
        else:
            result = {'success':False}
      except anvil.users.TooManyPasswordFailures as e:
          # Do something in response to the exception
          result = {'success':False, 'message':'Твърде много опити'}
      except anvil.users.EmailNotConfirmed as e:
          result = {'success':False, 'message':'🙀 Непотвърдена ел. поща'}
      except anvil.users.AuthenticationFailed as e:
          result = {'success':False, 'message':'🙀 Некоректна парола или ел. поща'}

      return result