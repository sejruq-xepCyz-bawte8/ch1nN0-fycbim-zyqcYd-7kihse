from anvil import *
from .._FormTemplate import _FormTemplate
from anvil_extras.storage import indexed_db
import re
from ...Index.App import GENRES, AW
from anvil_extras.Autocomplete import Autocomplete
from anvil_extras.ChipsInput import ChipsInput
from anvil_extras.Chip import Chip

"""
    'микро разказ':{'level':1,'desc':'', 'wmin':0, 'wmax': 100,'parents':['проза']}, #up to 100 words
    'флашфикшън':{'level':1,'desc':'', 'wmin':101, 'wmax': 1000,'parents':['проза']}, #100 to 1,000 words
    'разказ':{'level':1,'desc':'', 'wmin':1001, 'wmax': 7500,'parents':['проза']}, #1,000 to 7,500 words
    'повест':{'level':1,'desc':'', 'wmin':7501, 'wmax': 17000,'parents':['проза']}, #7,500 то 17,500words
    'новела':{'level':1,'desc':'', 'wmin':17001, 'wmax': 40000,'parents':['проза']}, #17,500 to 40,000 words
    'роман':{'level':1,'desc':'', 'wmin':40001, 'wmax': 999999,'parents':['проза']}, #40к - 100к

# poetry
    'стих':{'level':1,'desc':'', 'pmin':0, 'pmax': 5,'parents':['поезия']},
    'хайку':{'level':1,'desc':'', 'pmin':3, 'pmax': 4,'parents':['поезия']},
    'стихотворение':{'level':1,'desc':'', 'pmin':6, 'pmax': 50,'parents':['поезия']},
    'епос':{'level':1,'desc':'', 'pmin':50, 'pmax': 999999,'parents':['поезия']},
"""


class Editor_Tags(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
    self.editor_store = indexed_db.create_store('editor')
    self.words = self.editor_store['words']
    self.html_work = self.editor_store['html']
    self.icon_keywords = []
    self.genres = []
    
  def show_form(self, **event):
    
    words = self.editor_store['words']
    p_all = self.count_par(self.html_work)
    p_sent = self.count_par_end_sentences(self.html_work)
    p_cent = self.count_par_centered(self.html_work)
    
    if words < 100 : genres = ['микро разказ', 'хайку', 'стих']
    elif words < 1000 : genres = ['флашфикшън', 'стихотворение']
    elif words < 7500 : genres = ['разказ', 'приказка', 'епос']
    elif words < 17000 : genres = ['повест']
    elif words < 40000 : genres = ['новела']
    else : genres = ['роман']
    
    prob_genre = genres[0] if p_sent > p_all / 2 or p_cent < p_all / 2 else genres[-1]
 

    self.add_div('Възможните типове на творбата се определят на базата брой думи, затова жанровете най-добре да се уточнят когато е завършен текста :). Ключовите думи са важни и за бъдещата търсачка, максимума им е 10')

    self.level1 = self.add_dropdown(items=genres, selected_value=prob_genre)
    self.level1.add_event_handler('change', self.level1_change)

    self.level2 = self.add_dropdown(items=GENRES.get_genre_names_by_level(level=2), include_placeholder=True, placeholder="Основен Жанр")
    self.level2.add_event_handler('change', self.level2_change)

    self.level3 = self.add_dropdown(items=[], include_placeholder=True, placeholder="Под Жанр", visible=False)
    self.level3.add_event_handler('change', self.level3_change)

    self.icon_keywords_choser = Autocomplete(suggestions=AW.get_all_names(), placeholder="Ключови думи (клик/ентер)")
    self.icon_keywords_choser.add_event_handler('pressed_enter', self.suggestion_clicked_enter)
    self.icon_keywords_choser.add_event_handler('suggestion_clicked', self.suggestion_clicked_enter)
    self.add_component(self.icon_keywords_choser)


    self.icon_chips = self.add_flowpanel()


  def icon_bar_build(self, sender=None, **event):
    icons = []
    if self.level1.selected_value: icons.append(self.level1.selected_value)
    if self.level2.selected_value: icons.append(self.level2.selected_value)
    if self.level3.selected_value: icons.append(self.level3.selected_value)
    self.icon_chips.clear()
    print(icons)
    for i in icons:
      if not i : continue
      aw = f'fa:{AW.get_name(bg=i)}'
      chip = Chip(text=i, icon=aw)
      chip.close_icon = False
      chip.background = "LightGreen"
      self.icon_chips.add_component(chip)
    c = 0
    for i in self.icon_keywords:
      aw = AW.get_name(bg=i)
      chip = Chip(text=i, icon=f'fa:{aw}')
      if aw != 'icons':
        c+=1
        chip.background = "LightBlue" if c <=3 else "LightGray"
      
      chip.add_event_handler('close_click', self.delete_keyword)
      self.icon_chips.add_component(chip)

  def delete_keyword(self, sender, **event):
    sender.remove_from_parent()
    keyword = sender.text
    self.icon_keywords.remove(keyword)
    self.icon_bar_build()

  def suggestion_clicked_enter(self, sender, **event):
    if len(self.icon_keywords) <= 10 and sender.text not in self.icon_keywords and sender.text is not "":
      self.icon_keywords.append(sender.text)
      sender.text = ''
      self.icon_bar_build()


  def level1_change(self, sender, **event):
    self.icon_bar_build()

  def level3_change(self, sender, **event):
    self.icon_bar_build()



  def level2_change(self, sender, **event):
    genres_level3 = GENRES.get_genre_children_names(genre_name=sender.selected_value)
    if len(genres_level3) > 0:
      self.level3.items = genres_level3
      self.level3.visible = True
    else:
      self.level3.items = []
      self.level3.visible = False
    self.icon_bar_build(self)

  @staticmethod
  def count_par_empty(html):
    pattern = r'<p[^>]*>\s*</p>'
    matches = re.findall(pattern, html)
    count = len(matches)
    return count  

  @staticmethod
  def count_par_end_sentences(html):
    pattern = r'[.!?]</p>'
    matches = re.findall(pattern, html)
    count = len(matches)
    return count

  @staticmethod
  def count_par_centered(html):
    pattern = r'ql-align-center'
    matches = re.findall(pattern, html)
    count = len(matches)
    return count

  @staticmethod
  def count_par(html):
    pattern = r'<p>'
    matches = re.findall(pattern, html)
    count = len(matches)
    return count

