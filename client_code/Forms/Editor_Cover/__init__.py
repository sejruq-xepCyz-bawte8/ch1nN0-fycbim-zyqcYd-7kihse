from anvil import *
from .._FormTemplate import _FormTemplate
from .CoverElement import CoverClass
from .Contrast import adjust_color_for_contrast
from .ImageCover import parse_cover_image
from .Fonts import fonts
from anvil.js.window import jQuery as jQ

contrast = 11
cover_data = {
  'title':'ЗАГЛАВИЕ на произведението',
  'genres':['проза', 'разказ', 'фантастика', 'научна'],
  'keywords':['днес', 'начало'],
  'background-image':None,
  'font':'serif',
  'background-color':'#FFFFFF',
  'color':'#000000',
  'cover_mask':30,
  'mask_color':'#DDDDDD'
}

no_data = {
  'title':'ЗАГЛАВИЕ на произведението',
  'genres':['проза', 'разказ', 'фантастика', 'научна'],
  'keywords':['днес', 'начало'],
  'background-image':None,
  'font':'serif',
  'background-color':'#FFFFFF',
  'color':'#000000',
  'cover_mask':30,
  'mask_color':'#DDDDDD'
}



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
    
    self.init_components(**properties)
    self.data = cover_data



  def show_form(self, **event):

    self.title = self.add_textbox(text=self.data['title'], placeholder='Заглавие', change=self.design_change)
    self.uri = self.add_textbox(placeholder='URI')
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
    

  def design_change(self, sender, **event):
    self.data['title'] = self.title.text
    self.data['uri'] = self.uri.text
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
    
    self.data['mask_color'] = adjust_color_for_contrast(self.data['color'], '000000', 100)


    self.cover_container.empty()
    self.cover = CoverClass(data=self.data)
    self.append_jq_el(element=self.cover.el, parent=self.cover_container)

