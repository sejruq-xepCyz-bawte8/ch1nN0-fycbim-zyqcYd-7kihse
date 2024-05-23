from .Template_Module import TemplateMemory
from datetime import datetime


class Authors(TemplateMemory):

  def __init__(self, collection: object, data: list):
    super().__init__(loki_collection=collection)
    if data:
      self.collection.insert(data)

  def filter_genre(self, genre:str=None):
    if genre:
      filter = { 'g' : { '$contains' : f'{genre}'} }
    else:
      filter = None
    result = self.collection.chain().find(filter).data({'removeMeta':True})
    
    return result
    
      

  
  def timestamp(self):
    now = datetime.now()
    year = now.year
    day_in_year = now.timetuple().tm_yday
    day_in_month = now.timetuple().tm_mday
    day_in_week = now.timetuple().tm_wday
    ts_day = year % 1000 * 1000 + day_in_year
    ts_week = ts_day - day_in_week
    ts_month = ts_day - day_in_month
    
    return {'d':ts_day, 'w':ts_week, 'm':ts_month, 'a':24000}