from anvil import *
from .._FormTemplate import _FormTemplate
from .ZodParse import code_zod, email_zod, password_zod
from .Login import login_user
from .SignUp import sign_up_new_user
from .LogOut import logout_user



class Settings_User(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    
  def show_form(self, **event):
    self.info_container = self.add_colpanel()
    self.info = self.add_label(text="Потребител", parent=self.info_container)
    if not self.is_user:
      self.login_signup_form()
    else:
      self.email = self.add_label(text=self.user_email)
      self.add_button(text="Изход", click=self.login_logout)
      
   
    
  def user_settings(self):
    pass

  def login_signup_form(self):
    self.login_choise = self.add_radio(name='form', text="Вход", selected=True, change=self.login_type_change)
    self.add_radio(name='form', text="Регистрация", change=self.login_type_change)
    
  #just login panel
    self.login_panel = self.add_colpanel()
    self.email = self.add_textbox(parent=self.login_panel, placeholder='Ел. Поща', change=email_zod)
    self.password = self.add_textbox(parent=self.login_panel, placeholder='Парола', hide_text=True, change=password_zod)
    
  #signup panel
    self.signup_panel = self.add_colpanel(visible=False)
    self.password2 = self.add_textbox(parent=self.signup_panel, placeholder='Потвърди Паролата', hide_text=True, change=self.check_password2)
    self.code = self.add_textbox(parent=self.signup_panel, placeholder='Код за регистрация', change=code_zod) 
    self.age = self.add_checkbox(parent=self.signup_panel, text="Пълнолетие", checked=False)
    self.terms = self.add_checkbox(parent=self.signup_panel, text="Съгласен съм с условията", checked=False, change=self.terms_change)
    self.terms_text = self.add_rich_markdown(parent=self.signup_panel, text=login_signup_welcome)


    ###################################

    self.email.valid = None
    self.password.valid = None
    self.password2.valid = None
    self.code.valid = None
    self.button = self.add_button(text="Вход", click=self.login_signup)
    self.sign_up_button_validation()
  

  def login_type_change(self, sender, **event):
    self.signup_panel.visible = not self.login_choise.selected
    self.button.text = "Вход" if self.login_choise.selected else "Регистрация"
    self.terms.checked = self.login_choise.selected
    self.sign_up_button_validation()


  def check_password2(self, sender, **event):
        sender.valid = True if sender.text is self.password.text and password_zod(sender=sender) else False
        sender.background = "LightGreen" if sender.valid else "LightSalmon"
        self.sign_up_button_validation()

  def terms_change(self, sender, **event):
    self.sign_up_button_validation()

  def login_logout(self, sender, **event):
    result = logout_user()
    self.info.text = result['message']

  def sign_up_button_validation(self):
    if  self.login_choise.selected: self.button.enabled = True
    elif self.password.valid and self.password2.valid and self.email.valid and self.code.valid and self.terms.checked:
      self.button.enabled = True
    else:
      self.button.enabled = False
  
  def login_signup(self, sender, **event):
    valid = None
    if not self.login_choise.selected:
      #validation register
      if self.password.valid and self.password2.valid and self.email.valid and self.code.valid and self.terms.checked:
        result = sign_up_new_user(self.email.text, self.password.text, self.code.text, self.age.checked)
        self.info.text = result['message']
    else:
      #login
      if self.email.valid and self.password.valid:
        valid = True
        result = login_user(self.email.text, self.password.text)
        self.info.text = result['message']
        



  def author_settings(self):
    pass






login_signup_welcome = """#### Четеме EULA"""