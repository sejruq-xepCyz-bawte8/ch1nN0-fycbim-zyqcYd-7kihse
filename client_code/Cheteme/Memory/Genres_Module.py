
from .Template_Module import TemplateMemory
from functools import lru_cache

class Genres(TemplateMemory):
  def __init__(self, collection: object, data: list):
    super().__init__(loki_collection=collection)
    if data:
      self.collection.insert(data)


 
  def genre_names_in_level(self, level):
    return self.get_column('bg', 'level', value=level)



  def genres_list_in_level(self, level):
    return self.get_list('level', value=level)
  

  def genre_subgenre_names(self, genre):
    gid = self.get_one(key='bg', value=genre)['gid']
    return self.get_column(column='bg', key='genre', value=gid)




  def genre_subgenres(self, genre):
    return self.get_list(key='genre', value=genre)
  
  
  def prose_by_words(self, words: int = 0) -> list:
    return self.get_column_between_keys(column='bg', value = words, key_min='wmin', key_max='wmax')

  @lru_cache(maxsize=None)
  def poetry_by_paragraphs(self, paragraphs: int = 0)  -> list:
    return self.get_column_between_keys(column='bg', value = paragraphs, key_min='pmin', key_max='pmax')
  
