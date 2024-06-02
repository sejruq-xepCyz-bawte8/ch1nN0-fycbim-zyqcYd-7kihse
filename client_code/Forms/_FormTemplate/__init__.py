from ._anvil_designer import _FormTemplateTemplate
from anvil import *
from anvil.js.window import jQuery as jQ

from ...Index.App import NAVIGATION, DEVICE_ID, USER_ID, AUTHOR_ID, USER


class _FormTemplate(_FormTemplateTemplate):
  def __init__(self, **properties):
    self.add_event_handler('show', self.show_form)
    self.form_name = self.__class__.__name__
    self.module_name = self.__class__.__module__.split(".")[1]
    self.package_name = __package__
    self.el = None
    self.is_user = bool(USER_ID)
    self.is_author = bool(AUTHOR_ID)
    self.is_device = bool(DEVICE_ID)
    self.user = USER_ID
    self.user_email = USER['email'] if USER else None
    self.author = AUTHOR_ID
    self.device = DEVICE_ID
    self.init_components(**properties)
    
  def init_form_element(self):

    self.el = jQ('#appGoesHere > .html-templated-panel')
    self.el.attr('id', f'form-{self.form_name}')
    self.el.addClass(f'form-{self.form_name}')
     

  def new_div(self, text:str=None, css_class:str=None)->object:
     if not self.el: self.init_form_element()
     if not css_class: css_class = ""
     element = jQ(f'<dir>')
     element.text(text)
     element.addClass(f'ch {css_class}')
     return element

  def add_div(self, text:str=None, css_class:str=None, parent:object=None)->object:
     if not self.el: self.init_form_element()
     if not parent : parent = self.el
     element = self.new_div(text=text, css_class=css_class)
     parent.append(element)
     return element



  def navClick(self, link, **event):
      NAVIGATION.click(link) #send back for visuals

      onclick = link.attr('data-onclick')
      if onclick == 'open_form':
         open_form(f"Forms.{link.attr('data-form')}") #open new form
         
      else:
         function_to_call = getattr(self, onclick) #find and fire func in cur form
         function_to_call()

  def show_form(self, **event):
      self.init_form_element()
      self.add_label(text=self.__name__)
   
  def click_back(self):
      pass

  
  def prep_anvil_element(self, parent, element, name, change=None, click=None):
      if change: element.add_event_handler('change', change)
      if click: element.add_event_handler('click', click)
      if name: setattr(self, name, element)
      self.add_component(element) if not parent else parent.add_component(element)
      return element

  def add_button(self,name:str = None,text:str = None,parent:object = None,
                 click = None,role:str = 'ch',visible = True,
                 ) -> Button:
     element = Button(text=text, role=role, visible=visible)
     return self.prep_anvil_element(parent=parent, element=element, name=name, click=click)

  def add_label(self,name:str = None,text:str = None,parent:object = None,
                role:str = 'ch',visible = True
                ) -> Label:
     element = Label(text=text, role=role, visible=visible)
     return self.prep_anvil_element(parent=parent, element=element, name=name)

  def add_checkbox(self,name:str = None,text:str = None,checked:bool = False,
                   parent:object = None,role:str = 'ch',visible = True, change = None,
                  ) -> CheckBox:
     element = CheckBox(text=text, checked=checked, role=role, visible=visible)
     return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)

  def add_radio(self, name:str = None, text:str = None,
                group_name:str = None, selected:bool = False,
                parent:object = None, role:str = 'ch',visible = True, change = None
                ) -> RadioButton:
      element = RadioButton(text=text, group_name=group_name, selected=selected, visible=visible, role=role)
      return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)

  def add_rich_markdown(self,name:str = None,text:str = None,parent:object = None,
                        role:str = 'ch',visible = True
                        ) -> RichText:
      element = RichText(content=text, role=role, visible=visible)
      return self.prep_anvil_element(parent=parent, element=element, name=name)


  def add_textbox(self, name:str = None, text:str = None, change = None, placeholder:str = None,
          parent:object = None, role:str = 'ch', hide_text = None, visible = True,
          ) -> TextBox:
   element = TextBox(text=text, placeholder=placeholder, role=role, hide_text=hide_text, visible=visible)
   return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)
  
  def add_colpanel(self, name:str = None, parent:object = None,role:str = 'ch',
                   visible = True
                  ) -> ColumnPanel:
   element = ColumnPanel(role=role, visible=visible)
   return self.prep_anvil_element(parent=parent, element=element, name=name)
