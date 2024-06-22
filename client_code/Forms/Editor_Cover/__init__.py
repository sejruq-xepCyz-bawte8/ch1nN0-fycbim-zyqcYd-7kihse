from anvil import *
from .._FormTemplate import _FormTemplate
from .CoverElement import CoverClass
from .Contrast import adjust_color_for_contrast
from .ImageCover import parse_cover_image
from .Fonts import fonts_list
from anvil.js.window import jQuery as jQ


from URI_parser import uri_zod, title_zod
from ...Index import App

contrast = 11

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

  def show_form(self, **event):
    title = App.EDITOR.data.get('title') or ''
    uri = App.EDITOR.data.get('work_uri') or ''
    
    self.title = self.add_textbox(text=title, placeholder='Заглавие', change=self.design_change)
    
    
    self.add_flowpanel(name='uri_panel')
    self.permalink = self.add_label(text=f'https://chete.me/{App.AUTHOR_URI}/', parent=self.uri_panel)
    self.uri = self.add_textbox(placeholder='URI: лат., цифри и -_~', text=uri, parent=self.uri_panel, change=self.design_change)
    

    self.cover_container = self.add_div(id='cover-container')
    self.cover = CoverClass(data=App.EDITOR.data)

    self.append_jq_el(element=self.cover.el, parent=self.cover_container)
    
    self.font_pane = self.add_flowpanel()
    self.font = self.add_dropdown(items=fonts_list, change=self.design_change, parent=self.font_pane)
    self.font.selected_value = App.EDITOR.data['font']
    self.prev_font = self.add_button(text='<', parent=self.font_pane, click=self.font_button)
    self.next_font = self.add_button(text='>', parent=self.font_pane, click=self.font_button)

    spacer = Spacer()
    self.add_component(spacer)

    self.colors_el = jQ(colors_html)
    jQ('#color').val(App.EDITOR.data['color'])
    jQ('#background-color').val(App.EDITOR.data['background_color'])
    jQ('#cover_mask').val(App.EDITOR.data['cover_mask'])
    jQ('#mask_color').val(App.EDITOR.data['mask_color'])

    self.append_jq_el(self.colors_el)
    
    spacer2 = Spacer()
    self.add_component(spacer2)

    self.add_flowpanel(name='files_panel')

    self.cover_upload = self.add_uploader(text='Ъплоад Корица', parent=self.files_panel, change=self.design_change)
    self.cover_delete = self.add_button(text='Изчисти Корица', parent=self.files_panel, click=self.design_change)


    self.design_change(sender=None)

  def design_change(self, sender, **event):
    uri_zod(self.uri)
    title_zod(self.title)

    App.EDITOR.data['title'] = self.title.text
    App.EDITOR.data['work_uri'] = self.uri.text
    App.EDITOR.data['font'] = self.font.selected_value

    if sender is 'color':
      App.EDITOR.data['color'] = jQ('#color').val()
      App.EDITOR.data['background_color'] = adjust_color_for_contrast(App.EDITOR.data['color'], App.EDITOR.data['background_color'], 11)
      jQ('#color').val(App.EDITOR.data['color'])
      jQ('#background-color').val(App.EDITOR.data['background_color'])
    if sender is 'background-color':
      App.EDITOR.data['background_color'] = jQ('#background-color').val()
      App.EDITOR.data['color'] = adjust_color_for_contrast(App.EDITOR.data['background_color'], App.EDITOR.data['color'], 11)
      jQ('#color').val(App.EDITOR.data['color'])
      jQ('#background-color').val(App.EDITOR.data['background_color'])
      
    App.EDITOR.data['cover_mask'] = jQ('#cover_mask').val()
    if sender is self.cover_upload:
      App.EDITOR.data['background_image'] = parse_cover_image(sender.file)
      sender.file.text = sender.file.name
    if sender is self.cover_delete:
      App.EDITOR.data['background_image'] = None
      self.cover_upload.text='Ъплоад Корица'

    App.EDITOR.data['mask_color'] = adjust_color_for_contrast(App.EDITOR.data['color'], '000000', 100)


    self.cover_container.empty()
    self.cover = CoverClass(data=App.EDITOR.data)
    self.append_jq_el(element=self.cover.el, parent=self.cover_container)

    App.EDITOR.update(full=False)


  def font_button(self, sender, **event):
    # Find the index of the selected element
    index = fonts_list.index(self.font.selected_value)

    if sender == self.next_font:
      self.font.selected_value = fonts_list[index + 1] if index < len(fonts_list) - 1 else fonts_list[0]
    elif sender == self.prev_font:
      self.font.selected_value = fonts_list[index - 1] if index > 0 else fonts_list[-1]
 
    self.design_change(sender=None)