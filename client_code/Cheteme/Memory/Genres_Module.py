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
{'bg':'Проза','gid':1, 'level':1,'desc':''},
{'bg':'Поезия', 'gid':2, 'level':1,'desc':''},

{'bg':'Фентъзи','gid':11, 'level':2,'desc':''},
{'bg':'Фантастика','gid':12, 'level':2,'desc':''},
{'bg':'Ужаси','gid':14, 'level':2,'desc':''},
{'bg':'Драма','gid':15, 'level':2,'desc':''},
{'bg':'Трилър','gid':16, 'level':2,'desc':''},
{'bg':'Крими','gid':17, 'level':2,'desc':''},
{'bg':'Исторически','gid':18, 'level':2,'desc':''},
{'bg':'Романс','gid':19, 'level':2,'desc':''},
{'bg':'Детски','gid':20, 'level':2,'desc':''},
{'bg':'Съвременни','gid':21, 'level':2,'desc':''},
{'bg':'Хумор','gid':22, 'level':2,'desc':''},
{'bg':'Приключенски','gid':23, 'level':2,'desc':''},
{'bg':'Действителни','gid':24, 'level':2,'desc':''},
{'bg':'Еротика','gid':25, 'level':2,'desc':''},

  #scifi12
{'bg':'научна', 'genre':12, 'gid':1210, 'level':3,'desc':'Научна фантастика'},
{'bg':'класическа','genre':12, 'gid':1212, 'level':3,'desc':'Класическа фантастика'},
{'bg':'киберпънк','genre':12, 'gid':1213, 'level':3,'desc':'Киберпънк фантастика'},
{'bg':'соларпънк','genre':12, 'gid':1214, 'level':3,'desc':'Соларпънк фантастика'},
{'bg':'стиймпънк','genre':12, 'gid':1215, 'level':3,'desc':'Стиймпънк фантастика'},
{'bg':'утопия','genre':12, 'gid':1216, 'level':3,'desc':'Фантастика - утопия'},
{'bg':'антиутопия','genre':12, 'gid':1217, 'level':3,'desc':'Фантастика - антиутопия'},
{'bg':'постапокалипсис','genre':12, 'gid':1218, 'level':3,'desc':'Постапокалиптична фантастика'},
{'bg':'биопънк','genre':12, 'gid':1219, 'level':3,'desc':'Биопънк фантастика'},
{'bg':'технотрилър','genre':12, 'gid':1220, 'level':3,'desc':'Фантастика технотрилър'},
{'bg':'шпионска','genre':12, 'gid':1221, 'level':3,'desc':'Шпионска фантастика'},
{'bg':'хумористична','genre':12, 'gid':1222, 'level':3,'desc':'Хумористична фантастика'},
{'bg':'супергерои','genre':12, 'gid':1223, 'level':3,'desc':'Фантастика със супергерои'},
{'bg':'военна','genre':12, 'gid':1224, 'level':3,'desc':'Военна фантастика'},

  #cryme17
{'bg':'Детективски','genre':17, 'gid':1710, 'level':3,'desc':'Детективско криминале'},
{'bg':'Психопати и убийци','genre':17, 'gid':1711, 'level':3,'desc':'Криминале с психопати убийци'},
{'bg':'Мистерии','genre':17, 'gid':1712, 'level':3,'desc':'Криминале с мистерии'},

#thriller16
{'bg':'Психопати и серийни убийци','genre':16, 'gid':1610, 'level':3,'desc':'Трилър с психопати убийци'},
{'bg':'Криминален','genre':16, 'gid':1611, 'level':3,'desc':'Криминален трилър'},
{'bg':'Техно','genre':16, 'gid':1612, 'level':3,'desc':'Техно трилър'},
{'bg':'Исторически','genre':16, 'gid':1613, 'level':3,'desc':'Исторически трилър'},
{'bg':'Психологически','genre':16, 'gid':1614, 'level':3,'desc':'Психологически трилър'},
{'bg':'Медицински','genre':16, 'gid':1615, 'level':3,'desc':'Медицински трилър'},
{'bg':'Шпионски','genre':16, 'gid':1616, 'level':3,'desc':'Шпионски трилър'},
{'bg':'Политически','genre':16, 'gid':1617, 'level':3,'desc':'Политически трилър'},
{'bg':'Романтичен','genre':16, 'gid':1618, 'level':3,'desc':'Романтичен трилър'},


  #contemp21
{'bg':'Експериментална','genre':21, 'gid':2110, 'level':3,'desc':''},
{'bg':'Поток на мисълта','genre':21, 'gid':2111, 'level':3,'desc':''},
{'bg':'Епистоларна','genre':21, 'gid':2112, 'level':3,'desc':''},
{'bg':'Мемоари','genre':21, 'gid':2113, 'level':3,'desc':''},
{'bg':'ЛГТБ+','genre':21, 'gid':2114, 'level':3,'desc':''},
{'bg':'Пътепис','genre':21, 'gid':2115, 'level':3,'desc':''},
{'bg':'Гурме','genre':21, 'gid':2116, 'level':3,'desc':''},
{'bg':'ЧикЛит','genre':21, 'gid':2117, 'level':3,'desc':''},
{'bg':'Феминизъм','genre':21, 'gid':2118, 'level':3,'desc':''},

  #drama15
{'bg':'Историческа драма','genre':15, 'gid':1510, 'level':3,'desc':''},
{'bg':'Военна драма','genre':15, 'gid':1511, 'level':3,'desc':''},
{'bg':'Любовна драма','genre':15, 'gid':1512, 'level':3,'desc':''},
{'bg':'Семейна сага','genre':15, 'gid':1513, 'level':3,'desc':''},
{'bg':'Политическа драма','genre':15, 'gid':1514, 'level':3,'desc':''},

#historical18
{'bg':'Исторически по действителни събития','genre':18, 'gid':1810, 'level':3,'desc':''},
{'bg':'Историческа фикция','genre':18, 'gid':1811, 'level':3,'desc':''},
{'bg':'Исторически романс','genre':18, 'gid':1812, 'level':3,'desc':''},
{'bg':'Исторически трилър','genre':18, 'gid':1813, 'level':3,'desc':''},
        ]