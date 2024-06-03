from functools import lru_cache

class GenresClass:
    def __init__(self) -> None:

        self.data:dict = GENRES_DATA
   
    @lru_cache(maxsize=100)
    def find_genre(self, bg:str)->dict:
        bg = bg.lower()
        return {bg:self.data[bg]} if bg in self.data else None

    @lru_cache(maxsize=100)
    def is_genre(self, bg:str)->bool:
        bg = bg.lower()
        return True if bg in self.data else False

    @lru_cache(maxsize=100)
    def get_genre_parents(self, bg:str)->list[dict]:
        genre = self.find_genre(bg)
        parents = []
        for parent_name in genre[bg]['parents']:
            parent_genre = self.find_genre(parent_name)
            if parent_genre : parents.append(parent_genre)
        return parents

    @lru_cache(maxsize=100)
    def get_genre_children(self, genre_name:str)->list[dict]:
        genre = self.find_genre(genre_name)
        if not genre : return None
        level = genre[genre_name]['level']
        children = []
        for key, value in self.data.items():
            if key == genre_name : continue
            parents = value['parents']
            if genre_name in parents or level in parents:
                children.append({key:value})
        return children

GENRES_DATA_ = {
    'проза':{'level':0, 'parents':[]},
    'разказ':{'level':1, 'parents':['проза']},
    'фантастика':{'level':2, 'parents':[0]},
    'фентъзи':{'level':2, 'parents':[0]},
    'научна фантастика':{'level':3, 'parents':[], 'parents':['фантастика']},
    'романс':{'level':3, 'parents':[], 'parents':[2]},
}


GENRES_DATA = {
    'проза':{'level':0, 'parents':[],'desc':''},
    'поезия':{'level':0, 'parents':[],'desc':''},
    'сборник проза':{'level':0, 'parents':[],'desc':''},
    'сборник поезия':{'level':0, 'parents':[],'desc':''}, 

# level 1
#prose
    'микро разказ':{'level':1,'desc':'', 'wmin':0, 'wmax': 100,'parents':['проза']}, #up to 100 words
    'флашфикшън':{'level':1,'desc':'', 'wmin':101, 'wmax': 1000,'parents':['проза']}, #100 to 1,000 words
    'разказ':{'level':1,'desc':'', 'wmin':1001, 'wmax': 7500,'parents':['проза']}, #1,000 to 7,500 words
    'повест':{'level':1,'desc':'', 'wmin':7501, 'wmax': 17000,'parents':['проза']}, #7,500 то 17,500words
    'новела':{'level':1,'desc':'', 'wmin':17001, 'wmax': 40000,'parents':['проза']}, #17,500 to 40,000 words
    'роман':{'level':1,'desc':'', 'wmin':40001, 'wmax': 999999,'parents':['проза']}, #40к - 100к

# poetry
    'стих':{'level':1,'desc':'', 'pmin':0, 'pmax': 5,'parents':['поезия']},
    'хайку':{'level':1,'desc':'', 'pmin':3, 'pmax': 4,'parents':['поезия']},
    'стихотворение':{'level':1,'desc':'', 'pmin':6, 'pmax': 50,'parents':['поезия']},
    'епос':{'level':1,'desc':'', 'pmin':50, 'pmax': 999999,'parents':['поезия']},

#genres - level2
    'еротика':{'level':2,'desc':'', 'parents':[1]},
    'фентъзи':{'level':2,'desc':'', 'parents':[1]},
    'фантастика':{'level':2,'desc':'', 'parents':[1]},
    'ужаси':{'level':2,'desc':'', 'parents':[1]},
    'драма':{'level':2,'desc':'', 'parents':[1]},
    'трилър':{'level':2,'desc':'', 'parents':[1]},
    'крими':{'level':2,'desc':'', 'parents':[1]},
    'исторически':{'level':2,'desc':'', 'parents':[1]},
    'романс':{'level':2,'desc':'', 'parents':[1]},
    'детски':{'level':2,'desc':'', 'parents':[1]},
    'съвременни':{'level':2,'desc':'', 'parents':[1]},
    'хумор':{'level':2,'desc':'', 'parents':[1]},
    'приключенски':{'level':2,'desc':'', 'parents':[1]},
    'действителни':{'level':2,'desc':'', 'parents':[1]},
#subgenres level3
#scifi
    'научна':{'level':3, 'parents':['фантастика'],'desc':'Научна фантастика'},
    'класическа':{'level':3, 'parents':['фантастика'],'desc':'Класическа фантастика'},
    'киберпънк':{'level':3, 'parents':['фантастика'],'desc':'Киберпънк фантастика'},
    'соларпънк':{'level':3, 'parents':['фантастика'],'desc':'Соларпънк фантастика'},
    'стиймпънк':{'level':3, 'parents':['фантастика'],'desc':'Стиймпънк фантастика'},
    'утопия':{'level':3, 'parents':['фантастика'],'desc':'Фантастика - утопия'},
    'антиутопия':{'level':3, 'parents':['фантастика'],'desc':'Фантастика - антиутопия'},
    'постапокалипсис':{'level':3, 'parents':['фантастика'],'desc':'Постапокалиптична фантастика'},
    'биопънк':{'level':3, 'parents':['фантастика'],'desc':'Биопънк фантастика'},
    'технотрилър':{'level':3, 'parents':['фантастика'],'desc':'Фантастика технотрилър'},
    'шпионска':{'level':3, 'parents':['фантастика'],'desc':'Шпионска фантастика'},
    'хумористична':{'level':3, 'parents':['фантастика'],'desc':'Хумористична фантастика'},
    'супергерои':{'level':3, 'parents':['фантастика'],'desc':'Фантастика със супергерои'},
    'военна':{'level':3, 'parents':['фантастика'],'desc':'Военна фантастика'},
#crime
    'детективски':{'level':3, 'parents':['крими'],'desc':'Детективско криминале'},
    'психопати и убийци':{'level':3, 'parents':['крими'],'desc':'Криминале с психопати убийци'},
    'мистерии':{'level':3, 'parents':['крими'],'desc':'Криминале с мистерии'},
#thriller
    'психопати и серийни убийци':{'level':3, 'parents':['трилър'],'desc':'Трилър с психопати убийци'},
    'криминален':{'level':3, 'parents':['трилър'],'desc':'Криминален трилър'},
    'техно':{'level':3, 'parents':['трилър'],'desc':'Техно трилър'},
    'исторически':{'level':3, 'parents':['трилър'],'desc':'Исторически трилър'},
    'психологически':{'level':3, 'parents':['трилър'],'desc':'Психологически трилър'},
    'медицински':{'level':3, 'parents':['трилър'],'desc':'Медицински трилър'},
    'шпионски':{'level':3, 'parents':['трилър'],'desc':'Шпионски трилър'},
    'политически':{'level':3, 'parents':['трилър'],'desc':'Политически трилър'},
    'романтичен':{'level':3, 'parents':['трилър'],'desc':'Романтичен трилър'},
#contemporary
    'експериментална':{'level':3, 'parents':['съвременни'],'desc':''},
    'поток на мисълта':{'level':3, 'parents':['съвременни'],'desc':''},
    'епистоларна':{'level':3, 'parents':['съвременни'],'desc':''},
    'мемоари':{'level':3, 'parents':['съвременни'],'desc':''},
    'лгтб+':{'level':3, 'parents':['съвременни'],'desc':''},
    'пътепис':{'level':3, 'parents':['съвременни'],'desc':''},
    'гурме':{'level':3, 'parents':['съвременни'],'desc':''},
    'чиклит':{'level':3, 'parents':['съвременни'],'desc':''},
    'феминизъм':{'level':3, 'parents':['съвременни'],'desc':''},
#drama
    'историческа драма':{'level':3, 'parents':['драма'],'desc':''},
    'военна драма':{'level':3, 'parents':['драма'],'desc':''},
    'любовна драма':{'level':3, 'parents':['драма'],'desc':''},
    'семейна сага':{'level':3, 'parents':['драма'],'desc':''},
    'политическа драма':{'level':3, 'parents':['драма'],'desc':''},
#historical
    'исторически по действителни събития':{'level':3, 'parents':[],'desc':''},
    'историческа фикция':{'level':3, 'parents':['исторически'],'desc':''},
    'исторически романс':{'level':3, 'parents':['исторически'],'desc':''},
    'исторически трилър':{'level':3, 'parents':['исторически'],'desc':''}
}

if __name__ == '__main__':
    test = GenresClass()
    #test.get_name.cache_clear()
    #print(test)
    print(test.get_genre_parents('разказ'))