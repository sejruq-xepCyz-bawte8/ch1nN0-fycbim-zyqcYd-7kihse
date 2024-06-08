from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import EDITOR
from ...PyScript.PyScriptLoader import has_pyscript, load_pyscript
from anvil_extras import non_blocking


def pyscript_defer_load():
   if not has_pyscript():load_pyscript()

non_blocking.defer(pyscript_defer_load, 0)

class Author_Works(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def draw_works(self, **event):
      self.clear()
      for work in EDITOR.all_works_data():
        container = self.add_flowpanel()
        

        button_o = self.add_button(parent=container, click=self.open_work)
        button_o.work_id = work['work_id']
        button_o.icon = 'fa:file-pen'



        self.add_label(parent=container, text=work['title'])

        button_d = self.add_button(parent=container, click=self.delete_work)
        button_d.work_id = work['work_id']
        button_d.icon = 'fa:file-xmark'

  def show_form(self, **event):
    self.draw_works()

  def open_work(self, sender, **event):
    result = EDITOR.set_current(work_id=sender.work_id)
    if result:
        self.navClick_by_id(link_id="#navl-Editor-Editor_Work", from_group="Author")

    
  def delete_work(self, sender, **event):
    result = EDITOR.delete_by_id(work_id=sender.work_id)
    if result:
       self.draw_works()
        




