from anvil import *
from .._FormTemplate import _FormTemplate

from ...Index.App import GENRES, AW
from anvil_extras.Autocomplete import Autocomplete

from anvil_extras.Chip import Chip

from .GuessGenres import guess_genres
from time import time

from ...Index.App import EDITOR

CHIP_BG = {
    0:['LightSalmon', 'LightGreen'],
   1:['LightSalmon', 'LightGreen'],
   2:['LightSalmon', 'LightGreen'],
   3:['LightGray', 'LightGreen'],
   4:['LightBlue', 'LightGreen'],
}

class Editor_Tags(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    
    self.chip_panels = {}
    self.title_info = self.add_label(text=EDITOR.data['title'])
    for p in range(5):
        self.chip_panels[p] = self.add_flowpanel()

    self.keywords = Autocomplete(suggestions=AW.get_all_names(), placeholder="Ключови думи (клик/ентер)")
    self.keywords.add_event_handler('pressed_enter', self.new_keyword)
    self.keywords.add_event_handler('suggestion_clicked', self.new_keyword)
    self.add_component(self.keywords)

  def show_form(self, **event):
    self.level1()
    self.level2()
    self.level3()
    self.level4()
 


  def level0(self):
      level = 0
      genre = EDITOR.data['genres'][level]
      parent_genre = EDITOR.data['genres'][level+1]
      if parent_genre:
        parents = GENRES.get_genre_parent_names(bg=parent_genre)
        genre = parents[0]
        EDITOR.data['genres'][level] = genre
      else:
        EDITOR.data['genres'][level] = None
      EDITOR.update()

  def level1(self):
    level = 1
    genre = EDITOR.data['genres'][level]
    genres = guess_genres(words=EDITOR.data['words'])
    if genre and genre not in genres:
      genres += [genre]
    for g in genres:
        chip = self.add_chip(bg=g, level=level)
        chip.selected = True if g is genre else False
        if genre and g is genre:
            chip.visible = True
        elif genre and g is not genre:
            chip.visible = False
        else:
            chip.visible = True
        chip.background = CHIP_BG[level][1] if g is genre else CHIP_BG[level][0]
    if not EDITOR.data['genres'][level]:
       EDITOR.data['genres'][level] = genre
       EDITOR.update()
    
    self.level0()
   
  def level2(self):
    level = 2
    genre = EDITOR.data['genres'][level]
    genres = GENRES.get_genre_names_by_level(level=level)
    for g in genres:
        chip = self.add_chip(bg=g, level=level)
        chip.selected = True if genre and genre == g else False
        if genre and genre == g:
            chip.visible = True
        elif genre and genre is not g:
            chip.visible = False
        else:
            chip.visible = True

        chip.background = CHIP_BG[level][1] if genre and genre == g else CHIP_BG[level][0]

  def level3(self):
    level = 3
    genre = EDITOR.data['genres'][level]
    parent_genre = EDITOR.data['genres'][level-1]
    genres = GENRES.get_genre_children_names(genre_name=parent_genre)
    for g in genres:
        chip = self.add_chip(bg=g, level=level)
        chip.selected = True if genre and genre == g else False
        chip.visible = True if genre and genre == g else False
        chip.background = CHIP_BG[level][1] if genre and genre == g else CHIP_BG[level][0]

  def level4(self):
    level = 4
    keywords = EDITOR.data['keywords']
    icons = EDITOR.data['icons']
    for k in keywords:
        chip = self.add_chip(bg=k, level=level)
        chip.selected = True if k in icons else False
        chip.background = CHIP_BG[level][1] if k in icons else CHIP_BG[level][0]

  def add_chip(self, bg:str, level:int, selected=False):
      aw = f'fa:{AW.get_name(bg=bg)}'
      chip = Chip(text=bg, icon=aw)
      chip.close_icon = False
      chip.selected = selected
      chip.level = level
      if level == 4:
          chip.close_icon = True
          chip.add_event_handler('close_click', self.delete_keyword)
      chip.add_event_handler('click', self.chip_click)
      chip.background = CHIP_BG[level][0]
      self.chip_panels[level].add_component(chip)
      return chip
  

  def new_keyword(self, sender, **event):
    level = 4
    keyword = sender.text
    parent = self.chip_panels[level]
    neighbours = parent.get_components()
    if len(neighbours) > 10: neighbours[-1].remove_from_parent()
    self.add_chip(bg=keyword, level=level)
    neighbours = parent.get_components()
    EDITOR.data['keywords'] = [k.text for k in neighbours]
    EDITOR.update()

  def delete_keyword(self, sender, **event):
    level = 4
    parent = self.chip_panels[level]
    sender.remove_from_parent()
    neighbours = parent.get_components()
    EDITOR.data['keywords'] = [k.text for k in neighbours]
    EDITOR.data['icons'] = [i.text for i in neighbours if i.selected]
    EDITOR.update()


  def chip_click(self, sender, **event):
    level = sender.level
    genre = sender.text
    is_selected = sender.selected

    if level == 4 :
       return self.keyword_click(sender=sender)
    if level == 2 :
       sub_genres_parent = self.chip_panels[level+1]
       sub_genres_parent.clear()
       EDITOR.data['genres'][level+1] = None
       if not is_selected:
          new_subgenres_names = GENRES.get_genre_children_names(genre_name=genre)
          for ns in new_subgenres_names:
              self.add_chip(bg=ns, level=level+1)
    
    parent = sender.parent
    neighbours = parent.get_components()
    

    for n in neighbours:
       n.selected = False
       n.background = CHIP_BG[level][0]
       n.visible = is_selected

    sender.selected = not is_selected
    sender.visible = True
    sender.background = CHIP_BG[level][1] if sender.selected else CHIP_BG[level][0]


    
    EDITOR.data['genres'][level] = sender.text if not is_selected else None
    EDITOR.update()

    if level == 1: self.level0()




  def keyword_click(self, sender):
    level = sender.level
    is_selected = sender.selected
    parent = self.chip_panels[level]
    neighbours = parent.get_components()
    icons = [i for i in neighbours if i.selected]

    if len(icons) < 3 or is_selected:
      sender.selected = not is_selected
      sender.background = CHIP_BG[level][1] if sender.selected else CHIP_BG[level][0]
      EDITOR.data['icons'] = [i.text for i in neighbours if i.selected]
      EDITOR.update()