from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index.App import READER
from anvil.js.window import jQuery as jQ

class ViewerW_Cover(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    #self.add_label(text=self.form_name)


  
    #COVER Image
    
    #self.el.attr('id', 'navigation')
    
    #cover.css("width", "100%")
    #cover.css('background-color', READER.data['background-color'])
    if READER.data['background-image'] and len(READER.data['background-image'])>10:
      cover = jQ('<img>')
      cover.addClass('ch ch-cover-work-reader')
      cover.attr('src', READER.data['background-image']) #f'url("{self.data['background-image']}")'
      self.append_jq_el(element=cover)

    self.add_div(text=READER.data['title'])
    self.add_div(text=READER.data.get('description'))
    self.add_div(text=f"думи: {READER.data.get('words')}")
    genres = READER.data.get('genres')
    for genre in genres:
      self.add_div(text=genre)
    self.add_div(text=f"автор: {READER.data.get('author_id')}")