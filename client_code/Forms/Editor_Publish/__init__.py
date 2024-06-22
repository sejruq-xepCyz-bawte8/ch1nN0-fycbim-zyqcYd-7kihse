from anvil import *
from .._FormTemplate import _FormTemplate
from ...Index import App
import anvil.server
from time import sleep, time


class Editor_Publish(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    

  def show_form(self, **event):
    self.add_label(text="Проверка на творбата за публикуване:")
    title = App.EDITOR.data.get('title', None)
    genres = App.EDITOR.data.get('genres', None)
    keywords = App.EDITOR.data.get('keywords', None)
    work_uri = App.EDITOR.data.get('work_uri', None)
    uri = f"https://chete.me/{App.AUTHOR_URI}/{work_uri}"
    background_image = bool(App.EDITOR.data.get('background_image', None))
    words = App.EDITOR.data.get('words', None)
    size = int(App.EDITOR.data.get('size', 0) / 1024)

    self.info = self.add_colpanel()
    self.title = self.add_label(text=f'Заглавие: {title}', parent=self.info)
    self.genres = self.add_label(text=f'Жанрове: {genres}', parent=self.info)
    self.add_label(text=f'Кл. думи: {keywords}', parent=self.info)
    self.permalink = self.add_label(text=f'Пермалинк: {uri}', parent=self.info)
    self.add_label(text=f'Изобр. корица: {background_image}', parent=self.info)
    self.words = self.add_label(text=f'Брой думи: {words}', parent=self.info)
    self.size = self.add_label(text=f'Размер кб: {size}', parent=self.info)

    self.publush_button = self.add_button(text="Публикувай", click=self.publish)
  
    if size > 1024 :
      self.publush_button.enabled = False
      self.size.foreground = 'Red'
    if words < 1 :
      self.publush_button.enabled = False
      self.words.foreground = 'Red'
    if not title or len(title) < 2 :
      self.publush_button.enabled = False
      self.title.foreground = 'Red'
    if not genres[0] or not genres[1] or not genres[2]:
      self.publush_button.enabled = False
      self.genres.foreground = 'Red'
    if not work_uri :
      self.publush_button.enabled = False
      self.permalink.foreground = 'Red'

  def publish(self, sender, **event):
    self.add_div('Започна публикуването, изчакайте за резултата ...')
    print('publush click')

    if App.USER_ID:
      print('publush calling')
      App.EDITOR.data['ptime'] = time()
      task = anvil.server.call('publish_author_work', html=App.EDITOR.html, data=App.EDITOR.data)
  
      for t in range(60):
        sleep(3)
        if task.is_completed(): break
      result = task.get_return_value()
      if result:
         self.add_div(text='ГОТОВО всичко е успешно')
      else:
         self.add_div(text='ПРИКЛЮЧИ но с грешки')

