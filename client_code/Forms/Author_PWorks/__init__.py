from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import EDITOR
from ...PyScript.PyScriptLoader import has_pyscript, load_pyscript
from anvil_extras import non_blocking

from ...Index.App import AUTHOR_ID
from ...API.ReaderApi import api_author, api_work
import json

def pyscript_defer_load():
   if not has_pyscript():load_pyscript()

non_blocking.defer(pyscript_defer_load, 0)

class Author_PWorks(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
   
    self.init_components(**properties)
    self.author_data, _ = api_author(AUTHOR_ID)
    self.author_works = self.author_data.get('works')
    self.add_help_panel(text='Публикувани творби', help=HELP)
    self.works = self.add_colpanel()

  def draw_works(self, **event):
      self.works.clear()
      for uri, work_id in self.author_works.items():
     
        
        work_data, _= api_work(work_id)
        container = self.add_flowpanel(parent=self.works)
        if work_data:
          self.add_label(parent=container, text=uri)
          self.add_label(parent=container, text=work_data['title'])
          self.add_label(parent=container, text=work_data['ptime'])
        else:
          self.add_label(parent=container, text=uri)
          self.add_label(parent=container, text='липсваща онлайн')

  def show_form(self, **event):
      self.draw_works()

    

    #self.draw_works()

  def open_work(self, sender, **event):
    result = EDITOR.set_current(work_id=sender.work_id)
    if result:
        self.navClick_by_id(link_id="#navl-Editor-Editor_Work", from_group="Author")

    
  def delete_work(self, sender, **event):
    result = EDITOR.delete_by_id(work_id=sender.work_id)
    if result:
       self.draw_works()
        




HELP = """<p>Тук са публикуваните творби само. Т.е. тези които са достъпни публично от ЧетеМе</p>
<p>При зареждане на екрана се обновяват автоматично от сървъра в момента</p>"""