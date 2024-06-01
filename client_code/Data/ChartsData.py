from time import time
from random import randrange, sample
from datetime import date
from functools import lru_cache

@lru_cache(maxsize=200)
def generate_charts():
    gt = ['poetry', 'prose']
    gz = ['short', 'large']
    gg = ['scifi', 'fantasy', 'cryme', 'thriller']
    gs = ['modern', 'classic', 'punk', 'love']
    gk = ['vampire', 'alien', 'blood', 'love', 'adult']
    charts = []
    for i in range(300):
        t = time() - randrange(0,100,1) * 86_400
        t2 = t - randrange(0,100,1) * 86_400
        d = date.fromtimestamp(t)
        g = sample(gt, 1) + sample(gz, 1)+ sample(gg, 1) + sample(gs, 1) + sample(gk, 2)
        a = randrange(1,20,1)
        l = [randrange(0,22,1),randrange(0,22,1),randrange(0,22,1),randrange(0,22,1)]
        work = {
            't':[t,t2], 'w':f'{i}-{d}', 'a':f'a{a}',
            'all':l, 'day':l, 'week':l, 'month':l,
            'g':g, 
        }
        charts.append(work)
    return charts


charts = generate_charts()



charts_template = [
    {'t':[1716992667,1716992667], 'w':'id-29may', 'a':'author001',
     0:[10,11,20,0], 1:[10,11,20,0], 7:[10,11,20,0], 30:[10,11,20,0],
     'g':['poetry', 'scifi', 'scifi-classic'],
     },

    {'t':[1717080246,1717080246], 'w':'id-001', 'a':'author001',
     0:[10,11,20,0], 1:[10,11,20,0], 7:[10,11,20,0], 30:[10,11,20,0],
     'g':['prose', 'scifi', 'scifi-classic'],
     },

    {'t':[1717080246,1717080246], 'w':'id-002', 'a':'author001',
     0:[10,11,20,0], 1:[10,11,20,0], 7:[10,11,20,0], 30:[10,11,20,0],
     'g':['poetry', 'scifi', 'scifi-classic'],
     },
]

if __name__=="__main__":
    from time import time
    from datetime import date
    #print(time())

    ts=int(1717080246.322782) #time in seconds
    tmins = ts // 60 #time in minutes - 60
    thours = ts // 60 // 60 #time in hours - 3600
    tdays = ts // 60 // 60 // 24 # time in days - 86400
    tweeks = ts // 60 // 60 // 24 // 7 # time in weeks
    tmonths = ts // 60 // 60 // 24 // 30.44 # time in months
    tyears = ts // 60 // 60 // 24 // 365.2425 # time in years
    print(tmonths)
    current_date = date.fromtimestamp(ts)
    print(current_date.day)

class RelativeTime():
    def __init__(self, ts:int=None, t:float=None) -> None:
        if not ts and not t:
            t = time()
            ts = int(t)
        elif ts and not t:
            t = float(ts)
        elif not ts and t:
            ts = int(t)
        
        self.t = t
        self.ts = ts
        self.tmins = ts // 60 #time in minutes - 60
        self.thours = ts // 60 // 60 #time in hours - 3600
        self.tdays = ts // 60 // 60 // 24 # time in days - 86400
        self.tweeks = ts // 60 // 60 // 24 // 7 # time in weeks
        self.tmonths = ts // 60 // 60 // 24 // 30.44 # time in months
        self.tyears = ts // 60 // 60 // 24 // 365.2425 # time in years
        self.date = date.fromtimestamp(ts)
        self.month = self.date.month
        self.week = self.isocalendar()[1]
        self.year = self.date.year