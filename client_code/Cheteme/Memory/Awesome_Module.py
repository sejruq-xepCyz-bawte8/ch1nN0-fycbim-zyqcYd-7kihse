from anvil.js.window import awesomeColl

class Awesome:
  def __init__(self):
    self.collection = awesomeColl
    self.collection.insert(icons)

  def get_icon_code(self, bg):
    return self.get_one('bg', bg)

  def get_icon_bg(self, name):
    return self.get_one('name', name)

  def get_one(self, key, value):
    return self.collection.findOne({ key : value })

icons = [{'name':'home', 'bg':'Днес'},
         {'name':'glasses', 'bg':'Автори'},
         {'name':'books', 'bg':'Творби'},
         {'name':'bookmark', 'bg':'Отметки'},
         {'name':'user', 'bg':'Вход'},
         {'name':'sliders', 'bg':'Настройки'},
         {'name':'typewriter', 'bg':'Автор'},
         {'name':'file-plus', 'bg':'Създай'},
          {'name':'chart-simple', 'bg':'Стат'},
         {'name':'address-card', 'bg':'Профил'},
         {'name':'icons', 'bg':'Тест'},

         #genres
          {'bg':'Поезия', 'name':'music'},
          {'bg':'Проза', 'name':'book'},
          {'bg':'Фентъзи', 'name':'hat-wizard'},
          {'bg':'Фантастика', 'name':'starship'},
          {'bg':'Ужаси', 'name':'face-scream'},
          {'bg':'Драма', 'name':'masks-theater'},
          {'bg':'Трилър', 'name':'gun'},
          {'bg':'Крими', 'name':'handcuffs'},
          {'bg':'Исторически', 'name':'fort'},
          {'bg':'Романс', 'name':'shield-heart'},
          {'bg':'Детски', 'name':'teddy-bear'},
          {'bg':'Съвременни', 'name':'calendar-star'},
          {'bg':'Хумор', 'name':'face-grin-squint-tears'},
          {'bg':'Приключенски', 'name':'map-location'},
          {'bg':'Действителни', 'name':'badge-check'},
          {'bg':'Еротика', 'name':'venus-mars'},
        ]


