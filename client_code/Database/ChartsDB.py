from Templates.DatabaseTemplate import DatabaseTemplateClass
from Data.ChartsData import charts
from functools import lru_cache
from time import time
from math import floor

class WorksDatabaseClass(DatabaseTemplateClass):
    def __init__(self, data) -> None:
        super().__init__(data=data)

    print('Charts Init')
    def get_work(self, value=str):
       w = self.search('wid', value=value)
       return w
    
    
    def filter_eng_today(self):
        days_past:int=0
        days_since_epoch = floor(time() // 86_400) # 60sec // 60min // 24h
        days_search = days_since_epoch - days_past
        t = days_search * 86_400
        filtered_data = [item for item in self.data if item['t'][0] >= t]
        return filtered_data

    def filter_eng_week(self):
        days_past:int=7
        days_since_epoch = floor(time() // 86_400) # 60sec // 60min // 24h
        days_search = days_since_epoch - days_past
        t = days_search * 86_400
        filtered_data = [item for item in self.data if item['t'][0] >= t]
        return filtered_data

    def get_genres(self):
        set_collect = set()
        for item in self.data:
            set_collect = set_collect | set(item['g'])
        return list(set_collect)
    
    def get_authors(self):
        set_collect = set()
        for item in self.data:
            set_collect.add(item['a'])
        return list(set_collect)

    def get_result(self, timestamp:str='eng', period:str='all', engagement:str=None, keywords:list=None):
        timestamp_dict = {'eng':0, 'pub':1}
        periods_dict = {'all':9999, 'day':0, 'week':7, 'month':30}
        engagements_dict = {'open':0, 'read':1, 'like':2, 'comment':3}
        
        if timestamp in timestamp_dict:
            t = timestamp_dict[timestamp]
        else:
            print('wrong timestamp')
            t = timestamp_dict['eng']


        if period in periods_dict:
            days_past = periods_dict[period]
        else:
            print('wrong period')
            days_past = periods_dict['all']

        days_since_epoch = floor(time() // 86_400) # 60sec // 60min // 24h
        days_search = days_since_epoch - days_past
        time_since_period = days_search * 86_400
        filtered_period = [item for item in self.data if item['t'][t] >= time_since_period]

        if keywords:
            print('keywords', keywords)
            filtered = [item for item in filtered_period if set(keywords).issubset(set(item['g']))]
        else:
            print('no keywords')
            filtered = filtered_period

        if engagement and engagement in engagements_dict:
            e = engagements_dict[engagement]
            sorted_data = sorted(filtered, key=lambda x: (x[period][e],x[period][2],x[period][3],x['t'][t]) , reverse=True) #(x['period'], x['key2']))
        else:
            print('wrong engagement')
            sorted_data = sorted(filtered, key=lambda x: (x['t'][t]), reverse=True)

        result = [{item['w']:item[period]} for item in sorted_data]
        return result



if __name__ == "__main__":
    
    

    test = WorksDatabaseClass(charts)

    import os
    os.system('clear')
    
    result = test.get_result(engagement='like', period='week')
    genres = test.get_authors()
    print(genres)
    