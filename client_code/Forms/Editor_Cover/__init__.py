from anvil import *
from .._FormTemplate import _FormTemplate
from .CoverElement import CoverClass
from .Contrast import adjust_color_for_contrast
from .ImageCover import parse_cover_image
from .Fonts import fonts
from anvil.js.window import jQuery as jQ
from anvil_extras.storage import indexed_db
from time import time
from URI_parser import encode_uri, uri_zod
contrast = 11

META_STORE = indexed_db.create_store('editor_meta')



colors_html = """
  <div class="ch-publish-design">
    <div>Цветове:</div>
    <label for="color"><input type="color" id="color" name="colors" value="#000000" onchange="anvil.call(this, 'design_change', this.id)"/>Текст</label>    
    <label for="background"><input type="color" id="background-color" name="colors" value="#FFFFFF" onchange="anvil.call(this, 'design_change', this.id)"/>Фон</label>
    <div>Сила на маската:</div>
    <input type="range" min="0" max="100" value="0" class="slider" id="cover_mask" onchange="anvil.call(this, 'design_change', this.id)">
  </div>
  """

class Editor_Cover(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.work_id = META_STORE['CURRENT']
    self.init_components(**properties)
    self.data = META_STORE[self.work_id]



  def show_form(self, **event):

    self.title = self.add_textbox(text=self.data['title'], placeholder='Заглавие', change=self.design_change)
    
    self.uri = self.add_textbox(placeholder='URI', change=self.design_change)
    self.uri.text = self.data['work_uri']
    uri_zod(self.uri)

    self.permalink = self.add_label(text='https://chete.me...')

    self.cover_container = self.add_div(id='cover-container')
    self.cover = CoverClass(data=self.data)

    self.append_jq_el(element=self.cover.el, parent=self.cover_container)
    
    self.font = self.add_dropdown(items=fonts.keys(), change=self.design_change)
    self.font.selected_value = self.data['font']

    self.colors_el = jQ(colors_html)
    jQ('#color').val(self.data['color'])
    jQ('#background-color').val(self.data['background-color'])
    jQ('#cover_mask').val(self.data['cover_mask'])
    jQ('#mask_color').val(self.data['mask_color'])

    self.append_jq_el(self.colors_el)
    self.cover_upload = self.add_uploader(text='Ъплоад Корица', change=self.design_change)
    self.cover_delete = self.add_button(text='Изчисти Корица', click=self.design_change)

  def design_change(self, sender, **event):
    self.data['title'] = self.title.text
    self.data['work_uri'] = self.uri.text
    uri_zod(self.uri)

    self.data['font'] = self.font.selected_value
    if sender is 'color':
      self.data['color'] = jQ('#color').val()
      self.data['background-color'] = adjust_color_for_contrast(self.data['color'], self.data['background-color'], 11)
      jQ('#color').val(self.data['color'])
      jQ('#background-color').val(self.data['background-color'])
    if sender is 'background-color':
      self.data['background-color'] = jQ('#background-color').val()
      self.data['color'] = adjust_color_for_contrast(self.data['background-color'], self.data['color'], 11)
      jQ('#color').val(self.data['color'])
      jQ('#background-color').val(self.data['background-color'])
      
    self.data['cover_mask'] = jQ('#cover_mask').val()
    if sender is self.cover_upload:
      self.data['background-image'] = parse_cover_image(sender.file)
      sender.file.text = sender.file.name
    if sender is self.cover_delete:
      self.data['background-image'] = None
      self.cover_upload.text='Ъплоад Корица'

    self.data['mask_color'] = adjust_color_for_contrast(self.data['color'], '000000', 100)


    self.cover_container.empty()
    self.cover = CoverClass(data=self.data)
    self.append_jq_el(element=self.cover.el, parent=self.cover_container)

    self.update_meta()


  def update_meta(self):
     self.data['mtime'] = time()
     META_STORE[self.work_id] = self.data