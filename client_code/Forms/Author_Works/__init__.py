from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
from ...PyScript.PyScriptLoader import has_pyscript, load_pyscript
from anvil_extras import non_blocking


def pyscript_defer_load():
   if not has_pyscript():load_pyscript()

non_blocking.defer(pyscript_defer_load, 0)

class Author_Works(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.add_help_panel(text='Чернови на това устройство', help=HELP)
    self.works = self.add_colpanel()
    

  def draw_works(self, **event):
      self.works.clear()
      works = []
      try:
        works = App.EDITOR.all_works_data()
      except :
        works = []
        
      for work in works:
        container = self.add_flowpanel(parent=self.works)
        

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
    result = App.EDITOR.set_current(work_id=sender.work_id)
    if result:
        self.navClick_by_id(link_id="#navl-Editor-Editor_Work", from_group="Author")

    
  def delete_work(self, sender, **event):
    result = App.EDITOR.delete_by_id(work_id=sender.work_id)
    if result:
       self.draw_works()
        




HELP = """<p>Тук са творбите създавани е редактирани на това устройство и браузер.</p>
<p>Те не се съхраняват никъде другаде.</p>
<p>При публикуване на творба, същата изпраща съдържанието си за публикуване.</p>
<p>Ако след това я редактирате или изтриете това няма да се отрази на Публикуваната и респ. Онлайн версия.</p>
<p>За да се отразят промени в Публикуваната творбата тук трябва да се публикува изрично отново.</p>"""