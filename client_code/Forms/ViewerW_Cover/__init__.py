from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
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
    #cover.css('background-color', App.READER.data['background-color'])
    if App.READER.data['background_image']:
      image_url = f'https://chete.me/?api=image&id={App.READER.data["wid"]}' 
      cover = jQ('<img>')
      cover.addClass('ch ch-cover-work-reader')
      cover.attr('src', image_url) #f'url("{self.data['background-image']}")'
      self.append_jq_el(element=cover)

    self.add_div(text=App.READER.data['title'])
    self.add_div(text=App.READER.data.get('description'))
    self.add_div(text=f"думи: {App.READER.data.get('words')}")
    genres = App.READER.data.get('genres')
    for genre in genres:
      self.add_div(text=genre)
    author_id = App.READER.data.get('author_id')
    author_data = App.READER.get_author_data(author_id)
    author_name = author_data.get('author_name')
    self.add_div(text=f"автор: {author_name}")