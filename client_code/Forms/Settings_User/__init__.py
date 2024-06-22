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

    self.l_email = self.add_textbox(parent=self.login_form, placeholder='Ел. Поща', change=self.input_change)
    self.l_password = self.add_textbox(parent=self.login_form, placeholder='Парола', hide_text=True, change=self.input_change)
    self.l_button = self.add_button(text="Вход", click=self.login_click, parent=self.login_form)

    self.s_email = self.add_textbox(parent=self.signup_form, placeholder='Ел. Поща', change=self.input_change)
    self.s_password = self.add_textbox(parent=self.signup_form, placeholder='Парола', hide_text=True, change=self.input_change)
    self.s_password2 = self.add_textbox(parent=self.signup_form, placeholder='Парола', hide_text=True, change=self.input_change)
    self.s_code = self.add_textbox(parent=self.signup_form, placeholder='Код за регистрация', change=self.input_change)
    self.age = self.add_checkbox(parent=self.signup_form, text="Пълнолетие", checked=False, change=self.input_change)
    self.terms = self.add_checkbox(parent=self.signup_form, text="Съгласен съм с условията", checked=False, change=self.input_change)
    self.s_button = self.add_button(text="Регистрация", click=self.signup_click, parent=self.signup_form)

    self.l_button.enabled = False
    self.s_button.enabled = False

    self.input_change(sender=None)

  def input_change(self, sender, **event):
    email_zod(self.l_email)
    email_zod(self.s_email)
    password_zod(self.l_password)
    password_zod(self.s_password)
    password_zod(self.s_password2)
    code_zod(self.s_code)
    if self.s_password.text != self.s_password2.text:
      self.s_password2.valid = False
      self.s_password2.border = "1px solid LightSalmon"
    
    self.l_button.enabled = True if self.l_email.valid and self.l_password.valid else False
    self.s_button.enabled = True if self.s_email.valid and self.s_password.valid and self.s_password2.valid and self.s_code.valid and self.age.checked and self.terms.checked else False

  def login_click(self, sender, **event):
    result = login_user(self.l_email.text, self.l_password.text)
    print(result['message'])
    #self.notify(message = result['message'])
  def signup_click(self, sender, **event):
    result = sign_up_new_user(self.s_email.text, self.s_password.text, self.s_code.text, self.age.checked)
    self.notify(message = result['message'])

  def login_type_change(self, sender, **event):
    self.login_form.visible = True if sender.text == 'Вход' else False
    self.signup_form.visible = True if sender.text != 'Вход' else False





  def login_logout(self, sender, **event):
    result = logout_user()
    self.info.text = result['message']


  







login_signup_welcome = """#### Четеме EULA"""
