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

icons = [
        #menus
        {'name':'home', 'bg':'Днес'},
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

  #subgehres
  #фантастика
  {'bg':'научна', 'name':'atom'},
{'bg':'класическа', 'name':'robot'},
{'bg':'киберпънк', 'name':'space-station-moon-construction'},
{'bg':'соларпънк', 'name':'trillium'},
{'bg':'стиймпънк', 'name':'steam-symbol'},
{'bg':'утопия', 'name':'omega',},
{'bg':'антиутопия', 'name':'user-bounty-hunter'},
{'bg':'постапокалипсис', 'name':'house-chimney-crack'},
{'bg':'биопънк', 'name':'vial-virus'},
{'bg':'технотрилър', 'name':'raygun'},
{'bg':'шпионска', 'name':'radar'},
{'bg':'хумористична', 'name':''},
{'bg':'супергерои', 'name':'mask'},
{'bg':'военна', 'name':'jet-fighter-up'},
#cryme
{'bg':'Детективски', 'name':'user-secret'},
{'bg':'Психопати и серийни убийци', 'name':'hockey-mask'},
{'bg':'Мистерии', 'name':'block-question'},
#thriller
#{'bg':'Криминален', 'name':'handcuffs'},
{'bg':'Техно', 'name':'microchip'},
#{'bg':'Исторически', 'name':'fort'},
{'bg':'Психологически', 'name':'brain'},
#{'bg':'Медицински', 'name':'syringe'},
{'bg':'Шпионски', 'name':'syringe'},
{'bg':'Политически', 'name':'scale-unbalanced'},
{'bg':'Романтичен', 'name':'heart-pulse'},
#contemporary
{'bg':'Експериментална','name':'head-sgide-brain'},
{'bg':'Поток на мисълта','name':'brain-arrow-curved-right'},
{'bg':'Епистоларна','name':'minimize'},
{'bg':'Мемоари','name':'book-font'},
{'bg':'ЛГТБ+','name':'transgender'},
{'bg':'Пътепис','name':'globe-stand'},
{'bg':'Гурме','name':'pot-food'},
{'bg':'ЧикЛит','name':'candy'},
{'bg':'Феминизъм','name':'venus'},
#drama
{'bg':'Историческа','name':'crown'},
{'bg':'Военна','name':'person-military-to-person'},
{'bg':'Любовна','name':'heart-crack'},
{'bg':'Семейна сага','name':'family'},
{'bg':'Политическа','name':'podium-star'},
#historical
{'bg':'По действителни събития','name':'monument'},
{'bg':'Историческа фикция','name':'angel'},
#{'bg':'Исторически романс','name':'shield-heart'},
{'bg':'Исторически трилър','name':'chess'},
        ]


