from ._anvil_designer import AuthorsTemplate
from anvil import *
from ..._Cheteme.ElementsHtml.panels_works import create_panel, create_icon_panel_genres_en, create_icon_panel_bg_filter_list
from anvil.js.window import jQuery as jQ
from ..._Cheteme.Memory import authors
from ..._Cheteme.Main import navigation_click
from ..._Cheteme.ElementsHtml.VisitCard import VisitCardClass


class Authors(AuthorsTemplate):
  def __init__(self, **properties):
    
    self.navigation_click = navigation_click
    self.init_components(**properties)
    self.add_event_handler('show', self.show_form)

  def show_form(self, **event):
   all = authors.get_all()
   data = {}
   target_id = "#authors"
   genres_authors = []
   for a in all:
      data['g'] = []
      if 'g' in a:
         data['g'] = a['g']
         for item in a['g']:
            if item not in genres_authors:
               genres_authors.append(item)

      if 'sg' in a:
         data['g'] = a['sg']
      if 't' in a:
         data['g'] += a['t']
      if 'k' in a:
         data['g'] += a['k']
     
      data['title'] = a['title']
      vc = VisitCardClass(a)
      jQ(target_id).append(vc())

  
       
   def form_click(self):
      pass