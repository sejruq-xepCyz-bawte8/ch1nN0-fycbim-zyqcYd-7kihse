from ...Index.App import init_user
import anvil.users

def login_user(email, password):
      try:
        user = anvil.users.login_with_email(email=email, password=password, remember=True)
        if user:
            init = init_user()
        if init:
            result = {'success':True, 'message':f'Успешен вход: {user["email"]}'}
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