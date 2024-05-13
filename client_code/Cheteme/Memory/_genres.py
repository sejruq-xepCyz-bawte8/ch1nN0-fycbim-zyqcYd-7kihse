import anvil.server
genres = [
# to be used if collection of works in one file
{'bg':'проза','gid':'prose', 'level':0,'desc':''},
{'bg':'поезия','gid':'poetry', 'level':0,'desc':''},
{'bg':'сборник проза','gid':'prose_collection', 'level':0,'desc':''},
{'bg':'сборник поезия','gid':'poetry_collection', 'level':0,'desc':''}, 

# level 1
#prose
    {'bg':'микро разказ','gid':'microfiction', 'level':1,'desc':'', 'wmin':0, 'wmax': 100,'type':'prose'}, #up to 100 words
    {'bg':'флашфикшън','gid':'flashfiction', 'level':1,'desc':'', 'wmin':101, 'wmax': 1000,'type':'prose'}, #100 to 1,000 words
    {'bg':'разказ','gid':'storie', 'level':1,'desc':'', 'wmin':1001, 'wmax': 7500,'type':'prose'}, #1,000 to 7,500 words
    {'bg':'повест','gid':'novelette', 'level':1,'desc':'', 'wmin':7501, 'wmax': 17000,'type':'prose'}, #7,500 то 17,500words
    {'bg':'новела','gid':'novella', 'level':1,'desc':'', 'wmin':17001, 'wmax': 40000,'type':'prose'}, #17,500 to 40,000 words
    {'bg':'роман','gid':'novel', 'level':1,'desc':'', 'wmin':40001, 'wmax': 999999,'type':'prose'}, #40к - 100к

# poetry
    {'bg':'стих', 'gid':'short_poem', 'level':1,'desc':'', 'pmin':0, 'pmax': 5,'type':'poetry'},
    {'bg':'хайку', 'gid':'haiku', 'level':1,'desc':'', 'pmin':3, 'pmax': 4,'type':'poetry'},
    {'bg':'стихотворение', 'gid':'poem', 'level':1,'desc':'', 'pmin':6, 'pmax': 50,'type':'poetry'},
    {'bg':'епос', 'gid':'epic_poem', 'level':1,'desc':'', 'pmin':50, 'pmax': 999999,'type':'poetry'},

#genres - level2
    {"bg":"еротика","gid":"erotica","level":2,"desc":""},
    {"bg":"фентъзи","gid":"fantasy","level":2,"desc":""},
    {"bg":"фантастика","gid":"scifi","level":2,"desc":""},
    {"bg":"ужаси","gid":"horror","level":2,"desc":""},
    {"bg":"драма","gid":"drama","level":2,"desc":""},
    {"bg":"трилър","gid":"thriller","level":2,"desc":""},
    {"bg":"крими","gid":"crime","level":2,"desc":""},
    {"bg":"исторически","gid":"historical","level":2,"desc":""},
    {"bg":"романс","gid":"romance","level":2,"desc":""},
    {"bg":"детски","gid":"children","level":2,"desc":""},
    {"bg":"съвременни","gid":"contemporary","level":2,"desc":""},
    {"bg":"хумор","gid":"humor","level":2,"desc":""},
    {"bg":"приключенски","gid":"adventure","level":2,"desc":""},
    {"bg":"действителни","gid":"realistic","level":2,"desc":""},
#subgenres level3
#scifi
    {"bg":"научна","genre":"scifi","gid":"scifi-science","level":3,"desc":"Научна фантастика"},
    {"bg":"класическа","genre":"scifi","gid":"scifi-classic","level":3,"desc":"Класическа фантастика"},
    {"bg":"киберпънк","genre":"scifi","gid":"scifi-cyberpunk","level":3,"desc":"Киберпънк фантастика"},
    {"bg":"соларпънк","genre":"scifi","gid":"scifi-solarpunk","level":3,"desc":"Соларпънк фантастика"},
    {"bg":"стиймпънк","genre":"scifi","gid":"scifi-steampunk","level":3,"desc":"Стиймпънк фантастика"},
    {"bg":"утопия","genre":"scifi","gid":"scifi-utopia","level":3,"desc":"Фантастика - утопия"},
    {"bg":"антиутопия","genre":"scifi","gid":"scifi-dystopia","level":3,"desc":"Фантастика - антиутопия"},
    {"bg":"постапокалипсис","genre":"scifi","gid":"scifi-postapocalyptic","level":3,"desc":"Постапокалиптична фантастика"},
    {"bg":"биопънк","genre":"scifi","gid":"scifi-biopunk","level":3,"desc":"Биопънк фантастика"},
    {"bg":"технотрилър","genre":"scifi","gid":"scifi-technothriller","level":3,"desc":"Фантастика технотрилър"},
    {"bg":"шпионска","genre":"scifi","gid":"scifi-spy","level":3,"desc":"Шпионска фантастика"},
    {"bg":"хумористична","genre":"scifi","gid":"scifi-humorous","level":3,"desc":"Хумористична фантастика"},
    {"bg":"супергерои","genre":"scifi","gid":"scifi-superheroes","level":3,"desc":"Фантастика със супергерои"},
    {"bg":"военна","genre":"scifi","gid":"scifi-military","level":3,"desc":"Военна фантастика"},
#crime
    {"bg":"детективски","genre":"crime","gid":"crime-detective","level":3,"desc":"Детективско криминале"},
    {"bg":"психопати и убийци","genre":"crime","gid":"crime-psychopaths","level":3,"desc":"Криминале с психопати убийци"},
    {"bg":"мистерии","genre":"crime","gid":"crime-mysteries","level":3,"desc":"Криминале с мистерии"},
#thriller
    {"bg":"психопати и серийни убийци","genre":"thriller","gid":"thriller-psychopaths","level":3,"desc":"Трилър с психопати убийци"},
    {"bg":"криминален","genre":"thriller","gid":"thriller-crime","level":3,"desc":"Криминален трилър"},
    {"bg":"техно","genre":"thriller","gid":"thriller-techno","level":3,"desc":"Техно трилър"},
    {"bg":"исторически","genre":"thriller","gid":"thriller-historical","level":3,"desc":"Исторически трилър"},
    {"bg":"психологически","genre":"thriller","gid":"thriller-psychological","level":3,"desc":"Психологически трилър"},
    {"bg":"медицински","genre":"thriller","gid":"thriller-medical","level":3,"desc":"Медицински трилър"},
    {"bg":"шпионски","genre":"thriller","gid":"thriller-spy","level":3,"desc":"Шпионски трилър"},
    {"bg":"политически","genre":"thriller","gid":"thriller-political","level":3,"desc":"Политически трилър"},
    {"bg":"романтичен","genre":"thriller","gid":"thriller-romantic","level":3,"desc":"Романтичен трилър"},
#contemporary
    {"bg":"експериментална","genre":"contemporary","gid":"contemporary-experimental","level":3,"desc":""},
    {"bg":"поток на мисълта","genre":"contemporary","gid":"contemporary-consciousness_stream","level":3,"desc":""},
    {"bg":"епистоларна","genre":"contemporary","gid":"contemporary-epistolary","level":3,"desc":""},
    {"bg":"мемоари","genre":"contemporary","gid":"contemporary-memoirs","level":3,"desc":""},
    {"bg":"лгтб+","genre":"contemporary","gid":"contemporary-lgbt","level":3,"desc":""},
    {"bg":"пътепис","genre":"contemporary","gid":"contemporary-travelogue","level":3,"desc":""},
    {"bg":"гурме","genre":"contemporary","gid":"contemporary-culinary","level":3,"desc":""},
    {"bg":"чиклит","genre":"contemporary","gid":"contemporary-chicklit","level":3,"desc":""},
    {"bg":"феминизъм","genre":"contemporary","gid":"contemporary-feminism","level":3,"desc":""},
#drama
    {"bg":"историческа драма","genre":"drama","gid":"drama-historical","level":3,"desc":""},
    {"bg":"военна драма","genre":"drama","gid":"drama-military","level":3,"desc":""},
    {"bg":"любовна драма","genre":"drama","gid":"drama-romance","level":3,"desc":""},
    {"bg":"семейна сага","genre":"drama","gid":"drama-family_saga","level":3,"desc":""},
    {"bg":"политическа драма","genre":"drama","gid":"drama-political","level":3,"desc":""},
#historical
    {"bg":"исторически по действителни събития","genre":"historical","gid":"historical-true_events","level":3,"desc":""},
    {"bg":"историческа фикция","genre":"historical","gid":"historical-fiction","level":3,"desc":""},
    {"bg":"исторически романс","genre":"historical","gid":"historical-romance","level":3,"desc":""},
    {"bg":"исторически трилър","genre":"historical","gid":"historical-thriller","level":3,"desc":""}
]