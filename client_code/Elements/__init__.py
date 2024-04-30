from functools import lru_cache
from .Card import Card

@lru_cache
def new_card(item, work_id='demo'):
  return Card(work_id=item)