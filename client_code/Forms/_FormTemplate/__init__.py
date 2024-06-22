from ._anvil_designer import _FormTemplateTemplate
from anvil import *
from anvil.js.window import jQuery as jQ

from ...Index import App


class _FormTemplate(_FormTemplateTemplate):
  def __init__(self, **properties):
    self.add_event_handler('show', self.show_form)
    self.form_name = self.__class__.__name__
    self.module_name = self.__class__.__module__.split(".")[1]
    self.package_name = __package__
    self.el = None
    self.is_user = App.IS_USER
    self.is_author = App.IS_AUTHOR
    self.is_device = App.IS_DEVICE
    self.user_id = App.USER_ID
    self.user_email = App.USER_EMAIL
    self.author_id = App.AUTHOR_ID
    self.device_id = App.DEVICE_ID
    self.init_components(**properties)
    
  def init_form_element(self):
    self.el = jQ('#appGoesHere > .html-templated-panel')
    self.el.attr('id', f'form-{self.form_name}')
    self.el.addClass(f'form-{self.form_name}')
     

  def new_div(self, text:str=None, css_class:str=None, id:str=None)->object:
     if not self.el: self.init_form_element()
     if not css_class: css_class = ""
     element = jQ(f'<dir>')
     element.text(text)
     element.addClass(f'ch {css_class}')
     if id : element.attr('id', id)
     return element

  def add_div(self, text:str=None, css_class:str=None, parent:object=None, id:str=None)->object:
     if not self.el: self.init_form_element()
     if not parent : parent = self.el
     element = self.new_div(text=text, css_class=css_class, id=id)
     parent.append(element)
     return element

  def append_jq_el(self, element:object, parent:object=None)->None:
     if not self.el: self.init_form_element()
     if not parent : parent = self.el
     parent.append(element)
     
  def navClick_by_id(self, link_id:str=None, from_group:str=None):
      link = jQ(link_id)
      if from_group:
        link.attr('data-current_group', from_group)
      self.navClick(link=link)
     

  def navClick(self, link, **event):
      App.NAVIGATION.click(link) #send back for visuals
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
      if name:
         setattr(self, name, element)
         element.name = name
      self.add_component(element) if not parent else parent.add_component(element)
      return element

  def add_button(self,name:str = None,text:str = None,parent:object = None,
                 click = None,role:str = 'ch',visible = True,
                 ) -> Button:
     element = Button(text=text, role=role, visible=visible)
     return self.prep_anvil_element(parent=parent, element=element, name=name, click=click)
  
  def add_link(self,name:str = None,text:str = None,parent:object = None,
                 click = None,role:str = 'ch',visible = True,
                 ) -> Link:
     element = Link(text=text, role=role, visible=visible)
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

  def add_rich_html(self,name:str = None,text:str = None,parent:object = None,
                        role:str = 'ch',visible = True
                        ) -> RichText:
      element = RichText(content=text, role=role, visible=visible, format='restricted_html')
      return self.prep_anvil_element(parent=parent, element=element, name=name)

  def add_textbox(self, name:str = None, text:str = None, change = None, placeholder:str = None,
          parent:object = None, role:str = 'ch', hide_text = None, visible = True
          ) -> TextBox:
   element = TextBox(text=text, placeholder=placeholder, role=role, hide_text=hide_text, visible=visible)
   return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)
  
  def add_colpanel(self, name:str = None, parent:object = None,role:str = 'ch',
                   visible = True
                  ) -> ColumnPanel:
   element = ColumnPanel(role=role, visible=visible)
   return self.prep_anvil_element(parent=parent, element=element, name=name)

  def add_flowpanel(self, name:str = None, parent:object = None,role:str = 'ch',
                     visible = True, align='left'
                     ) -> FlowPanel:
      element = FlowPanel(role=role, visible=visible, align=align, vertical_align='middle', spacing='tiny', spacing_above='none', spacing_below='none')
      return self.prep_anvil_element(parent=parent, element=element, name=name)

  def add_image(self, name:str = None, parent:object = None,role:str = 'ch',
                source=None, width=None, height=None,
                  visible = True
                     ) -> Image:
      element = Image(role=role, source=source, visible=visible, width=None, height=None)
      return self.prep_anvil_element(parent=parent, element=element, name=name)
  
  def add_uploader(self, name:str = None, parent:object = None,role:str = 'ch',
                text:str=None, visible = True, change=None
                     ) -> FileLoader:
      if not text : text = "Зареди"
      element = FileLoader(role=role, visible=visible, text=text)
      return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)
  
  def add_dropdown(self, name:str = None, parent:object = None,role:str = 'ch',
                selected_value:str=None, items:list = None, visible = True,
                placeholder:str=None,
                change=None
                     ) -> DropDown:
      if not items: items = []
      include_placeholder = False
      if placeholder: include_placeholder = True
      element = DropDown(role=role, visible=visible, selected_value=selected_value, items=items, include_placeholder=include_placeholder, placeholder=placeholder)
      return self.prep_anvil_element(parent=parent, element=element, name=name, change=change)
  
  def add_help_panel(self, name:str = None, parent:object = None,role:str = 'ch',
                     visible = True, align='justify', text=None, help=None
                     ) -> FlowPanel:
      element = ColumnPanel(role=role, visible=visible)
      header = FlowPanel(role=role, visible=visible, align=align, vertical_align='middle', spacing='tiny', spacing_above='none', spacing_below='none')
      element.add_component(header)
      self.add_label(parent=header, text=text)
      self.add_link(parent=header, text='Помощ', click=self.help_click)
      self.help_info = self.add_rich_html(parent=element, text=help, visible=False)

      return self.prep_anvil_element(parent=parent, element=element, name=name)

  def help_click(self, sender, **event):
     self.help_info.visible = not self.help_info.visible


  def notify(message:str, style='info', timeout=1.5):
        n = Notification(message, style=style, timeout=timeout)
        n.show()