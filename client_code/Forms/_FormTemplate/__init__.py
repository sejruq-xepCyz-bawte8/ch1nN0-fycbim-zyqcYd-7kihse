from ._anvil_designer import _FormTemplateTemplate
from anvil import *
from anvil.js.window import jQuery as jQ
from ...Index.App import NAVIGATION



class _FormTemplate(_FormTemplateTemplate):
  def __init__(self, **properties):
    self.add_event_handler('show', self.show_form)
    self.form_name = self.__class__.__name__
    self.module_name = self.__class__.__module__.split(".")[1]
    self.package_name = __package__
    self.el = None
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
     print('parent', parent)
     parent.append(element)
     return element



  def navClick(self, link, **event):
      id_components:list = link.attr('id').split('-')
      group_name:str = id_components[1]
      form_name:str = id_components[2]
      form_group:str = id_components[3]
      function_name = id_components[4]

      if function_name == 'open_form':
         open_form(f'Forms.{form_name}')
         NAVIGATION.click(link, group_name, form_name, form_group, function_name)
      else:
         function_to_call = getattr(self, function_name)
         function_to_call()
         NAVIGATION.click(link, group_name, form_name, form_group, function_name)
  def show_form(self, **event):
      self.init_form_element()
      self.add_label(text=self.__name__)
   
  def click_back(self):
      pass

  def add(self,
          type:object = None,
          name:str = None,
          text:str = None,
          placeholder:str = None,
          parent:object = None,
          click = None,
          change = None,
          role:str = 'ch'
          ) -> object:
      
      element = type()
      if text: element.text = text
      if text and type==RichText: element.content = text
      if placeholder: element.placeholder = placeholder
      if click: element.add_event_handler('click', click)
      if change: element.add_event_handler('change', change)
      if name: setattr(self, name, element)
      if role: element.role = role
      if parent:
         parent.add_component(element)
      else:
         self.add_component(element)


      return element


  def add_button(self,
          name:str = None,
          text:str = None,
          parent:object = None,
          click = None,
          role:str = 'ch'
          ) -> Button:
     
     return self.add(type=Button, name=name, text=text, parent=parent, click=click, role=role)

  def add_label(self,
          name:str = None,
          text:str = None,
          parent:object = None,
          role:str = 'ch'
          ) -> Label:
     
     return self.add(type=Label, name=name, text=text, parent=parent, role=role)



  