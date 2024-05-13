from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
from ...Cheteme.Main import navigation_click, user

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
      try:
        user = anvil.users.signup_with_email(self.email.text, self.password.text)
    
      except:
         print('error')


  def login_user(self):
      global user
      try:
        user = anvil.users.login_with_email(self.email.text, self.password.text)
      except anvil.users.TooManyPasswordFailures as e:
          # Do something in response to the exception
          self.info.text = "Твърде много опити"
      except anvil.users.AuthenticationFailed as e:
          self.info.text = "🙀 Некоректна парола или ел. поща"