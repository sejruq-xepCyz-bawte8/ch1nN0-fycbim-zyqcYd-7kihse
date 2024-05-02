import anvil.users
import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# when making new will not have id, when reading old will read by id
class Work:
  def __init__(self, **kwargs):
    if 'id' in kwargs and len(kwargs) == 1:
      self.load_work(kwargs['id'])
    else:
      self.set_attributes(self, kwargs)

  def load_work(self, work_id):
    self.record = app_tables.works.get_by_id(work_id=work_id)
    #check if no record ...

  def set_attributes(self, data):
    for key, value in data.items():
        setattr(self, key, value)