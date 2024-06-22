from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.Tabs import Tabs
from .ZodParse import code_zod, email_zod, password_zod
from .Login import login_user
from .SignUp import sign_up_new_user
from .LogOut import logout_user



class Settings_User(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)

  def tab_click(self, sender, **event):
    tab = sender.active_tab_index
    self.readers.visible = True if tab == 0  else False
    self.authors.visible = True if tab == 1  else False



  def build_readers(self, container):
    #READERS PANEL
    self.add_label(text='Можете да ползвате ЧетеМе, без нужда да се регистрирате.', parent=container)
    self.add_label(text='Ако искате да пренесете настройки, история и др. от това устройство в друго - следваща версия ще бъде добавена тази възможност :)', parent=container)


  def show_form(self, **event):

    if self.is_user:
      self.build_logged()
    else:
      self.tabs = Tabs(tab_titles=['Читател', 'Автор']) #tab_click
      self.tabs.add_event_handler('tab_click', self.tab_click)
      self.add_component(self.tabs)

      self.add_colpanel(name='readers')
      self.add_colpanel(name='authors', visible=False)

      self.build_readers(container=self.readers)
      self.login_signup_form(container=self.authors)

  def build_logged(self):
      self.clear()
      self.add_colpanel(name='logout_panel')
      self.email = self.add_label(text=self.user_email, parent=self.logout_panel)
      self.add_button(text="Изход", click=self.login_logout, parent=self.logout_panel)
  

  def login_signup_form(self, container):
    self.add_radio(name='choise', text="Вход", selected=True, change=self.login_type_change, parent=container)
    self.add_radio(name='choise', text="Регистрация", change=self.login_type_change, parent=container)
    self.add_colpanel(name='login_form', parent=container)
    self.add_colpanel(name='signup_form', parent=container, visible=False)

    self.l_email = self.add_textbox(parent=self.login_form, placeholder='Ел. Поща', change=email_zod)
    self.l_password = self.add_textbox(parent=self.login_form, placeholder='Парола', hide_text=True, change=password_zod)
    self.l_button = self.add_button(text="Вход", click=self.login_click, parent=self.login_form)

    self.s_email = self.add_textbox(parent=self.signup_form, placeholder='Ел. Поща', change=email_zod)
    self.s_password = self.add_textbox(parent=self.signup_form, placeholder='Парола', hide_text=True, change=password_zod)
    self.s_password2 = self.add_textbox(parent=self.signup_form, placeholder='Парола', hide_text=True, change=password_zod)
    self.s_code = self.add_textbox(parent=self.signup_form, placeholder='Код за регистрация', change=code_zod) 
    self.s_button = self.add_button(text="Регистрация", click=self.signup_click, parent=self.signup_form)


  def login_click(self):
    pass
  def signup_click(self):
    pass


  def login_type_change(self, sender, **event):
    self.login_form.visible = True if sender.text == 'Вход' else False
    self.signup_form.visible = True if sender.text != 'Вход' else False

    self.signup_panel.visible = not self.login_choise.selected
    self.button.text = "Вход" if self.login_choise.selected else "Регистрация"
    self.terms.checked = self.login_choise.selected
    self.sign_up_button_validation()


  def signup_formd(self, container):
  #just login panel
    self.login_panel = self.add_colpanel(parent=container)
    self.email = self.add_textbox(parent=self.login_panel, placeholder='Ел. Поща', change=email_zod)
    self.password = self.add_textbox(parent=self.login_panel, placeholder='Парола', hide_text=True, change=password_zod)
    
  #signup panel
    self.signup_panel = self.add_colpanel(visible=False, parent=container)
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
    self.button = self.add_button(text="Вход", click=self.login_signup, parent=container)
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
        if result.get('success'):
          self.authors.clear()
          self.build_authors(self.authors)






login_signup_welcome = """#### Четеме EULA"""
