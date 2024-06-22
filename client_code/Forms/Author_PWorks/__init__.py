from anvil import *
from .._FormTemplate import _FormTemplate
from ...PyScript.PyScriptLoader import has_pyscript, load_pyscript
from anvil_extras import non_blocking
from ...Index import App
from ...API.ReaderApi import api_author, api_work
import json

def pyscript_defer_load():
   if not has_pyscript():load_pyscript()

non_blocking.defer(pyscript_defer_load, 0)

class Author_PWorks(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
   
    self.init_components(**properties)
    #self.author_data, _ = api_author(App.AUTHOR_ID)
    #self.author_works = self.author_data.get('works')
    #self.author_works = App.AUTHOR_WORKS
    self.add_help_panel(text='Публикувани творби', help=HELP)
    self.works = self.add_colpanel()

  def draw_works(self, **event):
      self.works.clear()
      for uri, work_id in App.AUTHOR_WORKS.items():
        #work_data, _= api_work(work_id)
        container = self.add_flowpanel(parent=self.works)
        self.add_label(parent=container, text=uri)



  def show_form(self, **event):
      if App.AUTHOR_WORKS:
         self.draw_works()



  def open_work(self, sender, **event):
    result = App.EDITOR.set_current(work_id=sender.work_id)
    if result:
        self.navClick_by_id(link_id="#navl-Editor-Editor_Work", from_group="Author")

    
  def delete_work(self, sender, **event):
    result = App.EDITOR.delete_by_id(work_id=sender.work_id)
    if result:
       self.draw_works()
        




HELP = """<p>Тук са публикуваните творби само. Т.е. тези които са достъпни публично от ЧетеМе</p>
<p>При зареждане на екрана се обновяват автоматично от сървъра в момента</p>"""