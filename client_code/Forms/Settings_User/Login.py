from ...Index.App import init_user
import anvil.server
import anvil.users

def login_user(self):
      print("will try to login now")
      try:
        user = anvil.users.login_with_email(self.email.text, self.password.text)
        if user:
            init = init_user(user)
        if init:
            result = {'success':True}
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