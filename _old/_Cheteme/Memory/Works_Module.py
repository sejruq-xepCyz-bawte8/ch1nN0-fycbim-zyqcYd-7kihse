from .Template_Module import TemplateMemory
from datetime import datetime


class Works(TemplateMemory):

  def __init__(self, collection: object, data: list):
    super().__init__(loki_collection=collection)
    if data:
      self.collection.insert(data)


  def get_last_authors(self, n:int=999999, engagement:str='r', period:str = 'a', filters:dict = None):
      result, additional = self.get_last(n=n, engagement=engagement, period=period, filters=filters)
      
      aggregate = {}
      col_master = f'{engagement}{period}'
     
      for item in result:
         au = item['au']
         key = item[col_master]
         if au in aggregate:
            aggregate[au] += key
         else:
            aggregate[au] = key
      
      unique_au = [{'au': au, col_master: key} for au, key in aggregate.items()]
      sorted_au = sorted(unique_au, key=lambda x: x[col_master] , reverse=True)
      return sorted_au
      


  def get_last(self, n:int=10, engagement:str='r', period:str = 'a', filters:dict = None):
      timestamp = self.timestamp()[period]
      filter = {'t': {'$gte': timestamp}}
      if filters:
         for key, value in filters.items():
            filter[key] = value

      col_master = f'{engagement}{period}'
      if engagement == 'l':
         col_second = f'r{period}'
      else:
         col_second = f'l{period}'
      
      additional = []
      sort_result = [[col_master, 'true'], [col_second, 'true']]
      sort_additional = [['t', 'true'],[col_master, 'true'], [col_second, 'true']]
      

      result = self.collection.chain().find(filter).compoundsort(sort_result).limit(n).data({'removeMeta':True})
      #result = [{'w':r['w'], 't':r['t'], col_master:r[col_master], col_second:r[col_second]} for r in result]
      k = len(result)
      if k < n:
         n2 = n-k
         filter['t'] = {'$lt': timestamp}
         additional = self.collection.chain().find(filter).compoundsort(sort_additional).limit(n2).data({'removeMeta':True})
         #additional = [{'w':r['w'], 't':r['t'], col_master:r[col_master], col_second:r[col_second]} for r in additional]
      return result, additional
  
  

     



  def count_items(self):
     count = self.collection.chain().find().count()
     return count




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
  

