import anvil.server
import anvil.users
from functools import lru_cache

#@lru_cache(maxsize=100)
def get_work(work_id='demo'):
  return demo_work



demo_work = {'title':'demowork', 'genre': 1, 'subgenre': 2, 'keywords': [3,5,7] }


def clear_cache(interval):
    get_work.cache_clear()