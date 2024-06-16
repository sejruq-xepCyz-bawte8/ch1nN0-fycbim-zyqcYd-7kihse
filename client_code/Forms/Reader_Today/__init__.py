from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import READER
from ..Editor_Cover.CoverElement import CoverClass
from anvil.js.window import jQuery as jQ

class Reader_Today(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text=self.form_name)
    self.cover_container = self.add_div(id='cover-container')
    
    for w in READER.today:
      wid = next(iter(w))
      
      work_data = READER.get_work_data(wid)
      if work_data['background-image'] == True:
        work_data['background-image'] = f'https://images.chete.me/{wid}'
      cover = CoverClass(work_data)
      cover.el.attr('onclick', f'anvil.call($("#appGoesHere > div"), "open_work", {wid})')
      self.append_jq_el(element=cover.el, parent=self.cover_container)
    
    



  def open_work(self, sender, *event):
    wid = 0
    READER.set_current_work = wid
    form_id = ''
    self.navClick_by_id(form_id)

