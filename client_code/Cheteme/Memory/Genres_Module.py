from .Collection_Module import Collection


class Genres(Collection):
  def __init__(self):
    super().__init__()
    self.collection.insert(genres)

  def get_genre_code(self, bg):
    return self.get_one('bg', bg)

  def get_genre_bg(self, name):
    return self.get_one('name', name)

genres = {
  'fantasy': {'genre':'Фентъзи', 'icon':'hat-wizard', 'code':'fantasy'},
  'scifi':{'genre':'Фантастика', 'icon':'starship', 'code':'scifi'},
  'horror':{'genre':'Ужаси', 'icon':'face-scream', 'code':'horror'},
  'drama':{'genre':'Драма', 'icon':'masks-theater', 'code':'drama'},
  'thriller':{'genre':'Трилър', 'icon':'gun', 'code':'thriller'},
  'crime':{'genre':'Крими', 'icon':'handcuffs', 'code':'crime'},
  'historical':{'genre':'Исторически', 'icon':'fort', 'code':'historical'},
  'romanse':{'genre':'Романс', 'icon':'shield-heart', 'code':'romanse'},
  'children':{'genre':'Детски', 'icon':'teddy-bear', 'code':'children'},
  'contemporary':{'genre':'Съвременни', 'icon':'calendar-star', 'code':'contemporary'},
  'humor':{'genre':'Хумор', 'icon':'face-grin-squint-tears', 'code':'humor'},
  'adventure':{'genre':'Приключенски', 'icon':'map-location', 'code':'adventure'},
  'real':{'genre':'Действителни', 'icon':'badge-check', 'code':'real'},
  'erotique':{'genre':'Еротика', 'icon':'venus-mars', 'code':'erotique'},
}

subgenres = {
  'scifi':[
    {'genre':'научна', 'icon':'atom', 'code':'scientific'},
    {'genre':'класическа', 'icon':'robot', 'code':'classic'},
    {'genre':'киберпънк', 'icon':'space-station-moon-construction', 'code':'cyberpunk'},
    {'genre':'соларпънк', 'icon':'trillium', 'code':'solarpunk'},
    {'genre':'стиймпънк', 'icon':'steam-symbol', 'code':'steampunk'},
    {'genre':'утопия', 'icon':'omega', 'code':'utopy'},
    {'genre':'антиутопия', 'icon':'user-bounty-hunter', 'code':'antiutopy'},
    {'genre':'постапокалипсис', 'icon':'house-chimney-crack', 'code':'postapocalipse'},
    {'genre':'биопънк', 'icon':'vial-virus', 'code':'biopunk'},
    {'genre':'технотрилър', 'icon':'raygun', 'code':'technothriller'},
    {'genre':'шпионска', 'icon':'radar', 'code':'spy'},
    {'genre':'хумористична', 'icon':'', 'code':'humor'},
    {'genre':'супергерои', 'icon':'mask', 'code':'superhero'},
    {'genre':'военна', 'icon':'jet-fighter-up', 'code':'military'}
  ],

'crime':[
  {'genre':'Детективски', 'icon':'user-secret', 'code':''},
  {'genre':'Психопати и серийни убийци', 'icon':'hockey-mask', 'code':''},
  {'genre':'Мистерии', 'icon':'block-question', 'code':''}
],

'thriller':[
  {'genre':'Психопати и серийни убийци', 'icon':'hockey-mask','code':''},
{'genre':'Криминален', 'icon':'handcuffs','code':''},
{'genre':'Техно', 'icon':'microchip','code':''},
{'genre':'Исторически', 'icon':'fort','code':''},
{'genre':'Психологически', 'icon':'brain','code':''},
{'genre':'Медицински', 'icon':'syringe','code':''},
{'genre':'Шпионски', 'icon':'syringe','code':''},
{'genre':'Политически', 'icon':'scale-unbalanced','code':''},
{'genre':'Романтичен', 'icon':'heart-pulse','code':''}
],

'contemporary':[
  {'genre':'Експериментална','icon':'head-side-brain','code':''},
{'genre':'Поток на мисълта','icon':'brain-arrow-curved-right','code':''},
{'genre':'Епистоларна','icon':'minimize','code':''},
{'genre':'Мемоари','icon':'book-font','code':''},
{'genre':'ЛГТБ+','icon':'transgender','code':''},
{'genre':'Пътепис','icon':'globe-stand','code':''},
{'genre':'Гурме','icon':'pot-food','code':''},
{'genre':'ЧикЛит','icon':'candy','code':''},
{'genre':'Феминизъм','icon':'venus','code':''}
],

'drama':[
  {'genre':'Историческа','icon':'crown','code':''},
{'genre':'Военна','icon':'person-military-to-person','code':''},
{'genre':'Любовна','icon':'heart-crack','code':''},
{'genre':'Семейна сага','icon':'family','code':''},
{'genre':'Политическа','icon':'podium-star','code':''}
],

'historical':[
  {'genre':'По действителни събития','icon':'monument','code':''},
{'genre':'Историческа фикция','icon':'angel','code':''},
{'genre':'Исторически романс','icon':'shield-heart','code':''},
{'genre':'Исторически трилър','icon':'chess','code':''}
],

}
