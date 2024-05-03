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

  #scifi12
{'bg':'научна', 'genre':12, 'gid':1210, 'level':3},
{'bg':'класическа','genre':12, 'gid':1212, 'level':3},
{'bg':'киберпънк','genre':12, 'gid':1213, 'level':3},
{'bg':'соларпънк','genre':12, 'gid':1214, 'level':3},
{'bg':'стиймпънк','genre':12, 'gid':1215, 'level':3},
{'bg':'утопия','genre':12, 'gid':1216, 'level':3},
{'bg':'антиутопия','genre':12, 'gid':1217, 'level':3},
{'bg':'постапокалипсис','genre':12, 'gid':1218, 'level':3},
{'bg':'биопънк','genre':12, 'gid':1219, 'level':3},
{'bg':'технотрилър','genre':12, 'gid':1220, 'level':3},
{'bg':'шпионска','genre':12, 'gid':1221, 'level':3},
{'bg':'хумористична','genre':12, 'gid':1222, 'level':3},
{'bg':'супергерои','genre':12, 'gid':1223, 'level':3},
{'bg':'военна','genre':12, 'gid':1224, 'level':3},

  #cryme17
{'bg':'Детективски','genre':17, 'gid':1710, 'level':3},
{'bg':'Психопати и убийци','genre':17, 'gid':1711, 'level':3},
{'bg':'Мистерии','genre':17, 'gid':1712, 'level':3},

#thriller16
{'bg':'Психопати и серийни убийци','genre':16, 'gid':1610, 'level':3},
{'bg':'Криминален','genre':16, 'gid':1611, 'level':3},
{'bg':'Техно','genre':16, 'gid':1612, 'level':3},
{'bg':'Исторически','genre':16, 'gid':1613, 'level':3},
{'bg':'Психологически','genre':16, 'gid':1614, 'level':3},
{'bg':'Медицински','genre':16, 'gid':1615, 'level':3},
{'bg':'Шпионски','genre':16, 'gid':1616, 'level':3},
{'bg':'Политически','genre':16, 'gid':1617, 'level':3},
{'bg':'Романтичен','genre':16, 'gid':1618, 'level':3},


  #contemp21
{'bg':'Експериментална','genre':21, 'gid':2110, 'level':3},
{'bg':'Поток на мисълта','genre':21, 'gid':2111, 'level':3},
{'bg':'Епистоларна','genre':21, 'gid':2112, 'level':3},
{'bg':'Мемоари','genre':21, 'gid':2113, 'level':3},
{'bg':'ЛГТБ+','genre':21, 'gid':2114, 'level':3},
{'bg':'Пътепис','genre':21, 'gid':2115, 'level':3},
{'bg':'Гурме','genre':21, 'gid':2116, 'level':3},
{'bg':'ЧикЛит','genre':21, 'gid':2117, 'level':3},
{'bg':'Феминизъм','genre':21, 'gid':2118, 'level':3},

  #drama15
{'bg':'Историческа драма','genre':15, 'gid':1510, 'level':3},
{'bg':'Военна драма','genre':15, 'gid':1511, 'level':3},
{'bg':'Любовна драма','genre':15, 'gid':1512, 'level':3},
{'bg':'Семейна сага','genre':15, 'gid':1513, 'level':3},
{'bg':'Политическа драма','genre':15, 'gid':1514, 'level':3},

#historical18
{'bg':'Исторически по действителни събития','genre':18, 'gid':1810, 'level':3},
{'bg':'Историческа фикция','genre':18, 'gid':1811, 'level':3},
{'bg':'Исторически романс','genre':18, 'gid':1812, 'level':3},
{'bg':'Исторически трилър','genre':18, 'gid':1813, 'level':3},
        ]

