from anvil.js.window import genresColl

class Genres:
  def __init__(self):
    self.collection = genresColl
    self.collection.insert(genres)

  def get_icon_code(self, bg):
    return self.get_one('bg', bg)

  def get_icon_bg(self, name):
    return self.get_one('name', name)

  def get_one(self, key, value):
    return self.collection.findOne({ key : value })

genres = [
  {'bg':'Проза','gid':1, 'level':1},
{'bg':'Поезия', 'gid':2, 'level':1},

{'bg':'Фентъзи','gid':11, 'level':2},
{'bg':'Фантастика','gid':12, 'level':2},
{'bg':'Ужаси','gid':14, 'level':2},
{'bg':'Драма','gid':15, 'level':2},
{'bg':'Трилър','gid':16, 'level':2},
{'bg':'Крими','gid':17, 'level':2},
{'bg':'Исторически','gid':18, 'level':2},
{'bg':'Романс','gid':19, 'level':2},
{'bg':'Детски','gid':20, 'level':2},
{'bg':'Съвременни','gid':21, 'level':2},
{'bg':'Хумор','gid':22, 'level':2},
{'bg':'Приключенски','gid':23, 'level':2},
{'bg':'Действителни','gid':24, 'level':2},
{'bg':'Еротика','gid':25, 'level':2},
        ]

