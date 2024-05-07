from anvil.js.window import awesomeColl

class Awesome:
  def __init__(self):
    self.collection = awesomeColl
    self.collection.insert(icons)

  def get_icon_code(self, bg):
    icon = self.get_one('bg', bg)
    if icon :
      return icon['name']
    else:
      return 'icons'

  def get_icon_bg(self, name):
    return self.get_one('name', name)

  def get_one(self, key, value):
    return self.collection.findOne({ key : value })


icons = [
#menus
    {'bg':'днес', 'name':'home'},
    {'bg':'автори', 'name':'glasses'},
    {'bg':'творби', 'name':'books'},
    {'bg':'отметки', 'name':'bookmark'},
    {'bg':'вход', 'name':'user'},
    {'bg':'настройки', 'name':'sliders'},
    {'bg':'автор', 'name':'typewriter'},
    {'bg':'създай', 'name':'file-plus'},
    {'bg':'стат', 'name':'chart-simple'},
    {'bg':'профил', 'name':'address-card'},
    {'bg':'тест', 'name':'icons'},
#genres
    {'bg':'поезия', 'name':'music'},
    {'bg':'проза', 'name':'book'},
    {'bg':'фентъзи', 'name':'hat-wizard'},
    {'bg':'фантастика', 'name':'starship'},
    {'bg':'ужаси', 'name':'face-scream'},
    {'bg':'драма', 'name':'masks-theater'},
    {'bg':'трилър', 'name':'gun'},
    {'bg':'крими', 'name':'handcuffs'},
    {'bg':'исторически', 'name':'fort'},
    {'bg':'романс', 'name':'shield-heart'},
    {'bg':'детски', 'name':'teddy-bear'},
    {'bg':'съвременни', 'name':'calendar-star'},
    {'bg':'хумор', 'name':'face-grin-squint-tears'},
    {'bg':'приключенски', 'name':'map-location'},
    {'bg':'действителни', 'name':'badge-check'},
    {'bg':'еротика', 'name':'venus-mars'},
#subgenres
    {'bg':'научна', 'name':'atom'},
    {'bg':'класическа', 'name':'robot'},
    {'bg':'киберпънк', 'name':'space-station-moon-construction'},
    {'bg':'соларпънк', 'name':'trillium'},
    {'bg':'стиймпънк', 'name':'steam-symbol'},
    {'bg':'утопия', 'name':'omega'},
    {'bg':'антиутопия', 'name':'user-bounty-hunter'},
    {'bg':'постапокалипсис', 'name':'house-chimney-crack'},
    {'bg':'биопънк', 'name':'vial-virus'},
    {'bg':'технотрилър', 'name':'raygun'},
    {'bg':'шпионска', 'name':'radar'},
    {'bg':'хумористична', 'name':''},
    {'bg':'супергерои', 'name':'mask'},
    {'bg':'военна', 'name':'jet-fighter-up'},
    {'bg':'детективски', 'name':'user-secret'},
    {'bg':'психопати и серийни убийци', 'name':'hockey-mask'},
    {'bg':'мистерии', 'name':'block-question'},
    {'bg':'техно', 'name':'microchip'},
    {'bg':'психологически', 'name':'brain'},
    {'bg':'шпионски', 'name':'syringe'},
    {'bg':'политически', 'name':'scale-unbalanced'},
    {'bg':'романтичен', 'name':'heart-pulse'},
    {'bg':'експериментална', 'name':'head-sgide-brain'},
    {'bg':'поток на мисълта', 'name':'brain-arrow-curved-right'},
    {'bg':'епистоларна', 'name':'minimize'},
    {'bg':'мемоари', 'name':'book-font'},
    {'bg':'лгтб+', 'name':'transgender'},
    {'bg':'пътепис', 'name':'globe-stand'},
    {'bg':'гурме', 'name':'pot-food'},
    {'bg':'чиклит', 'name':'candy'},
    {'bg':'феминизъм', 'name':'venus'},
    {'bg':'историческа', 'name':'crown'},
    {'bg':'военна', 'name':'person-military-to-person'},
    {'bg':'любовна', 'name':'heart-crack'},
    {'bg':'семейна сага', 'name':'family'},
    {'bg':'политическа', 'name':'podium-star'},
    {'bg':'по действителни събития', 'name':'monument'},
    {'bg':'историческа фикция', 'name':'angel'},
    {'bg':'исторически трилър', 'name':'chess'}
]