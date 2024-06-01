from functools import lru_cache

class AwesomeClass:
   def __init__(self) -> None:

      self.data:dict = AWESOME_DATA
   
   @lru_cache(maxsize=100)
   def get_name(self, bg:str):
         bg = bg.lower()
         if bg in self.data:
            return self.data[bg]
         else:
            return 'icons'

   #@lru_cache(maxsize=100)
   def get_css(self, bg:str, name:str=None, style:str=None)->str:
      if not style: style = 'light'
      if not name:
         name = self.get_name(bg)
      return f'fa-{style} fa-{name}'



STYLES = ['solid', 'regular', 'light', 'duotone', 'thin']





keywords = {
#menus
    'днес':'home',
    'автори':'glasses',
    'творби':'books',
    'отметки':'bookmark',
    'вход':'user',
    'настройки':'sliders',
    'автор':'typewriter',
    'създай':'file-plus',
    'стат':'chart-simple',
    'профил':'address-card',
    'тест':'icons',

#genres
    'поезия':'align-center',
    'проза':'align-left',
    'микро разказ':'t', #up to 100 words
    'флашфикшън':'s', #100 to 1,000 words
    'разказ':'m', #1,000 to 7,500 words
    'повест':'l', #7,500 то 17,500words
    'новела':'x', #17,500 to 40,000 words
    'роман':'h', #40к - 100к

    'стих':'s',
    'хайку':'t',
    'стихотворение':'m',
    'епос':'l',

  
    'фентъзи':'hat-wizard',
    'фантастика':'starship',
    'ужаси':'face-scream',
    'драма':'masks-theater',
    'трилър':'gun',
    'крими':'handcuffs',
    'исторически':'fort',
    'романс':'shield-heart',
    'детски':'teddy-bear',
    'съвременни':'calendar-star',
    'хумор':'face-grin-squint-tears',
    'приключенски':'map-location',
    'действителни':'badge-check',
    'еротика':'venus-mars',
#subgenres
    'научна':'atom',
    'класическа':'robot',
    'киберпънк':'space-station-moon-construction',
    'соларпънк':'trillium',
    'стиймпънк':'steam-symbol',
    'утопия':'omega',
    'антиутопия':'user-bounty-hunter',
    'постапокалипсис':'house-chimney-crack',
    'биопънк':'vial-virus',
    'технотрилър':'raygun',
    'шпионска':'radar',
    'хумористична':'',
    'супергерои':'mask',
    'военна':'jet-fighter-up',
    'детективски':'user-secret',
    'психопати и серийни убийци':'hockey-mask',
    'мистерии':'block-question',
    'техно':'microchip',
    'психологически':'brain',
    'шпионски':'syringe',
    'политически':'scale-unbalanced',
    'романтичен':'heart-pulse',
    'експериментална':'head-sgide-brain',
    'поток на мисълта':'brain-arrow-curved-right',
    'епистоларна':'minimize',
    'мемоари':'book-font',
    'лгтб+':'transgender',
    'пътепис':'globe-stand',
    'гурме':'pot-food',
    'чиклит':'candy',
    'феминизъм':'venus',
    'историческа':'crown',
#'военна':'person-military-to-person',
    'любовна':'heart-crack',
    'семейна сага':'family',
    'политическа':'podium-star',
    'по действителни събития':'monument',
    'историческа фикция':'angel',
    'исторически трилър':'chess'
}


AWESOME_DATA = {
#menus
    'днес':'home',
    'автори':'glasses',
    'творби':'books',
    'отметки':'bookmark',
    'вход':'user',
    'настр.':'sliders',
    'настройки':'sliders',
    'автор':'typewriter',
    'създай':'file-plus',
    'стат':'chart-simple',
    'профил':'address-card',
    'тест':'icons',
    'писател': 'typewriter',
    'нова' : 'file-plus',
    'статс':'chart-simple',
    'корица': 'hexagon-image',
    'текст':'keyboard',
    'публикувай':'paper-plane',
    'филтри':'filter',
    'инфо':'circle-info',
    'потребител':'user',
    'теми':'palette',
    'харесай':'comment-heart',
    'запази':'circle-bookmark',
    'съдържание':'square-list',
    'творба':'scroll',
    'назад':'chevrons-left',
    'жанр':'tags',




#genres
    'поезия':'align-center',
    'проза':'align-left',
    'микро разказ':'t', #up to 100 words
    'флашфикшън':'s', #100 to 1,000 words
    'разказ':'m', #1,000 to 7,500 words
    'повест':'l', #7,500 то 17,500words
    'новела':'x', #17,500 to 40,000 words
    'роман':'h', #40к - 100к

    'стих':'s',
    'хайку':'t',
    'стихотворение':'m',
    'епос':'l',

  
    'фентъзи':'hat-wizard',
    'фантастика':'starship',
    'ужаси':'face-scream',
    'драма':'masks-theater',
    'трилър':'gun',
    'крими':'handcuffs',
    'исторически':'fort',
    'романс':'shield-heart',
    'детски':'teddy-bear',
    'съвременни':'calendar-star',
    'хумор':'face-grin-squint-tears',
    'приключенски':'map-location',
    'действителни':'badge-check',
    'еротика':'venus-mars',
#subgenres
    'научна':'atom',
    'класическа':'robot',
    'киберпънк':'space-station-moon-construction',
    'соларпънк':'trillium',
    'стиймпънк':'steam-symbol',
    'утопия':'omega',
    'антиутопия':'user-bounty-hunter',
    'постапокалипсис':'house-chimney-crack',
    'биопънк':'vial-virus',
    'технотрилър':'raygun',
    'шпионска':'radar',
    'хумористична':'',
    'супергерои':'mask',
    'военна':'jet-fighter-up',
    'детективски':'user-secret',
    'психопати и серийни убийци':'hockey-mask',
    'мистерии':'block-question',
    'техно':'microchip',
    'психологически':'brain',
    'шпионски':'syringe',
    'политически':'scale-unbalanced',
    'романтичен':'heart-pulse',
    'експериментална':'head-sgide-brain',
    'поток на мисълта':'brain-arrow-curved-right',
    'епистоларна':'minimize',
    'мемоари':'book-font',
    'лгтб+':'transgender',
    'пътепис':'globe-stand',
    'гурме':'pot-food',
    'чиклит':'candy',
    'феминизъм':'venus',
    'историческа':'crown',
    #'военна':'person-military-to-person',
    'любовна':'heart-crack',
    'семейна сага':'family',
    'политическа':'podium-star',
    'по действителни събития':'monument',
    'историческа фикция':'angel',
    'исторически трилър':'chess'
}


if __name__ == "__main__":

  
  test = AwesomeClass()
  #test.get_name.cache_clear()
  #print(test)
  print(test.get_name('драма'))