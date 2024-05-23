from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
from ..._Cheteme.Main import navigation_click, update_user_navigation, user

choise = {
  True: "Регистрация",
  False: "Вход"
}

class Login(LoginTemplate):
  def __init__(self, **properties):
    
    self.navigation_click = navigation_click
    self.init_components(**properties)
    self.signup = CheckBox(text = "Регистрация")
    self.signup.add_event_handler('change', self.change_choise)
    self.email = TextBox(placeholder='ел. поща')
    self.password = TextBox(placeholder='парола')
    self.code = TextBox(placeholder='регистр. код', visible = False)
    self.login = Link(text="Вход")
    self.login.add_event_handler('click', self.login_parser)
    self.info = Label()
    
    self.add_component(self.signup)
    self.add_component(self.email)
    self.add_component(self.password)
    self.add_component(self.code)
    self.add_component(self.login)
    self.add_component(self.info)
  
  def change_choise(self, sender, **event):
    self.code.visible = not self.code.visible
    self.login.text = choise[self.code.visible]
    self.info.text = ""

  def login_parser(self, sender, **event):
    if self.code.visible:
      self.sign_up_user()
    else:
      self.login_user()
      

  def sign_up_user(self):
      global user
      result = anvil.server.call('sign_up', self.email.text, self.password.text, self.code.text)
      self.info.text = result['reason']
      user = result['user']


  def login_user(self):
      global user
      try:
        user = anvil.users.login_with_email(self.email.text, self.password.text)
        update_user_navigation(user)
        navigation_click(id='Reader.Settings')
        
      except anvil.users.TooManyPasswordFailures as e:
          # Do something in response to the exception
          self.info.text = "Твърде много опити"
      except anvil.users.EmailNotConfirmed as e:
          self.info.text = "🙀 Непотвърдена ел. поща"
      except anvil.users.AuthenticationFailed as e:
          self.info.text = "🙀 Некоректна парола или ел. поща"