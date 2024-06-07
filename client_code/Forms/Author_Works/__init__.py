from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.storage import indexed_db
from anvil.js.window import jQuery as jQ

META_STORE = indexed_db.create_store('editor_meta')
HTML_STORE = indexed_db.create_store('editor_html')
editor_form = jQ("#navl-Editor-Editor_Work")

class Author_Works(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.work_ids = META_STORE['ALL'] if 'ALL' in META_STORE else []


  def show_form(self, **event):
    for work_id in self.work_ids:
      container = self.add_flowpanel()
      title = self.add_label(parent=container)
      data = META_STORE[work_id]
      title.text = data['title'] if data['title'] != '' else 'Без заглавие'
      button = self.add_button(parent=container, click=self.open_work)
      button.work_id = work_id
      button.icon = 'fa:file-pen'

  def open_work(self, sender, **event):
    work_id = sender.work_id
    META_STORE['CURRENT'] = work_id
    self.navClick(editor_form)

    
    





