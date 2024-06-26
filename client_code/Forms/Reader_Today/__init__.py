from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
from ..Editor_Cover.CoverElement import CoverClass
from anvil.js.window import jQuery as jQ
from anvil.js import window, document
from time import sleep

class Reader_Today(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.uri = get_url_hash()
    window.history.replaceState({}, document.title, window.location.origin)

    

  def show_form(self, **event):
    #open if something
    if 'author' in self.uri:
      App.READER.set_current_author(self.uri['author'])
      self.navClick_by_id("#navl-Reader-ViewerA_Author")
    elif 'work' in self.uri:
      App.READER.set_current_work(self.uri['work'])
      self.navClick_by_id("#navl-Reader-ViewerW_Work")
    else:
      self.build_today()


  def build_today(self):
    self.add_div(text="Последно публикувани")
    self.cover_container = self.add_div(id='cover-container')
    if App.READER.today:
      self.show_works()
    else:
      self.first_time_info()
      for t in range(30):
        if App.READER.today:
          self.show_works()
          break
        sleep(2)



  def first_time_info(self):
    n = Notification('<i class="fa-duotone fa-spinner fa-spin"></i>първо зареждане', style="info", timeout=1.5)
    n.show()

    
  def show_works(self):
    for w in App.READER.today:
      wid = next(iter(w))
      
      work_data = App.READER.get_work_data(wid)
      if work_data['background_image'] == True:
        work_data['background_image'] = f'https://chete.me/?api=image&id={wid}'
      cover = CoverClass(work_data)
      #cover.attr('data-onclick', "open_work")
      cover.el.attr('onclick', f'anvil.call($("#appGoesHere > div"), "open_work", "{wid}")')
      self.append_jq_el(element=cover.el, parent=self.cover_container)


  def open_work(self, sender, *event):
    wid = sender
    App.READER.set_current_work(wid)
    self.navClick_by_id("#navl-Reader-ViewerW_Work")

