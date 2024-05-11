from functools import lru_cache
from .Cover import CoverClass

#@lru_cache(maxsize=None)

def cover_non_cached(data: dict) -> object:
  return CoverClass(data)


def cover_factory(data: dict) -> object:
  data['keywords'] = ','.join(data['keywords'])
  data = tuple(data.items())
  return cached_cover(data)


@lru_cache(maxsize=None)
def cached_cover(data):
  data = dict(data)
  
  if not 'title' in data:
    data['title'] = 'Заглавие'
  if not 'genre' in data:
    data['genre'] = 'жанр'
  if not 'subgenre' in data:
    data['subgenre'] = 'поджанр'
  if not 'id' in data:
    data['id'] = 'test_id'
  if not 'keywords' in data:
    data['keywords'] = ""
  if not 'cover' in data:
    data['cover'] = False
  
  return CoverClass(data)


if __name__ == "__main__":
  print(__name__)