from functools import lru_cache
from .GenresData import GENRES_DATA

class GenresClass:
    def __init__(self) -> None:

        self.data:dict = GENRES_DATA
   
    @lru_cache(maxsize=100)
    def find_genre(self, bg:str=None)->dict:
        if not bg : return None
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
    def get_genre_parent_names(self, bg:str)->list[str]:
        genre = self.find_genre(bg)
        return genre[bg]['parents']


    @lru_cache(maxsize=100)
    def get_genre_children_names(self, genre_name:str)->list[str]:
        genre = self.find_genre(genre_name)
        if not genre : return []
        level = genre[genre_name]['level']
        children = []
        for key, value in self.data.items():
            if key == genre_name : continue
            parents = value['parents']
            if genre_name in parents or level in parents:
                children.append(key)
        return children

    @lru_cache(maxsize=100)
    def get_genre_names_by_level(self, level:int)->list[str]:
            genres = []
            for key, value in self.data.items():
                if value['level'] is level:
                    genres.append(key)

            return genres

    @lru_cache(maxsize=100)
    def get_genre_level(self, bg:str)->int:
            genre = self.find_genre(bg=bg)
            level = genre[bg]['level']
            return level


if __name__ == '__main__':
    test = GenresClass()
    #test.get_name.cache_clear()
    #print(test)
    print(test.get_genre_names_by_level(1))