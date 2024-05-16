from datetime import datetime, timedelta


work_data =       {
    'id': 'test_id',
      'title': "Заглавие",
      'uri': "uri",
      'type': "тип",
      'keywords': [],
      'words': 0,
      'font':None,
      'shadow':None,
      'color':None,
      'background':None,
      'cover':None
}

works = [
    {'w':'today 11 22', 'pa':24135, 't':24135, 'ra':11, 'la':22, 'rd':11, 'ld':22, 'rw':22, 'lw':1550, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'today 22 11', 'pa':24135, 't':24135, 'ra':22, 'la':11, 'rd':22, 'ld':11, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'prose', 'wg':'crime', 'ws':'scifi-classic'},
    {'w':'yestd 33 33', 'pa':24134, 't':24134, 'ra':33, 'la':33, 'rd':33, 'ld':33, 'rw':10, 'lw':140, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'yestd 44 44', 'pa':24134, 't':24134, 'ra':44, 'la':44, 'rd':44, 'ld':44, 'rw':120, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'today 22 22', 'pa':24135, 't':24135, 'ra':22, 'la':22, 'rd':22, 'ld':22, 'rw':10, 'lw':140, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'thriller', 'ws':'scifi-classic'},
    {'w':'today 77 77', 'pa':24135, 't':24135, 'ra':77, 'la':77, 'rd':77, 'ld':77, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'today 77 99', 'pa':24135, 't':24135, 'ra':77, 'la':99, 'rd':77, 'ld':99, 'rw':10, 'lw':110, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'yestd 55 55', 'pa':24134, 't':24134, 'ra':55, 'la':55, 'rd':55, 'ld':55, 'rw':1220, 'lw':1330, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'yestd 77 77', 'pa':24134, 't':24134, 'ra':77, 'la':77, 'rd':77, 'ld':77, 'rw':10, 'lw':1330, 'rm':120, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'yestd 77 99', 'pa':24134, 't':24134, 'ra':99, 'la':99, 'rd':99, 'ld':99, 'rw':101, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past1 ', 'pa':24120, 't':24120, 'ra':110, 'la':10, 'rd':10, 'ld':10, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past11 ', 'pa':24120, 't':24120, 'ra':10, 'la':120, 'rd':10, 'ld':10, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past111 ', 'pa':24120, 't':24120, 'ra':1440, 'la':10, 'rd':10, 'ld':10, 'rw':10, 'lw':150, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past1 11 11', 'pa':24120, 't':24120, 'ra':151, 'la':11, 'rd':11, 'ld':11, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past1111 ', 'pa':24120, 't':24120, 'ra':10, 'la':1220, 'rd':10, 'ld':10, 'rw':10, 'lw':1660, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past2 ', 'pa':24121, 't':24121, 'ra':10, 'la':10, 'rd':10, 'ld':10, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'tempp ww ww', 'pa':24001, 't':24001, 'ra':120, 'la':110, 'rd':10, 'ld':10, 'rw':99, 'lw':99, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past22 ', 'pa':24121, 't':24121, 'ra':160, 'la':10, 'rd':10, 'ld':10, 'rw':10, 'lw':150, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past3 ', 'pa':24120, 't':24120, 'ra':1011, 'la':10, 'rd':10, 'ld':10, 'rw':10, 'lw':10, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'},
    {'w':'past33 99 99', 'pa':24120, 't':24120, 'ra':99, 'la':99, 'rd':99, 'ld':99, 'rw':99, 'lw':99, 'rm':10, 'lm':10, 'wt':'poetry', 'wg':'scifi', 'ws':'scifi-classic'}
   
]

if __name__ == "__main__":
    
    now = datetime.now()
    year = now.year
    day_in_year = now.timetuple().tm_yday
    day_in_month = now.timetuple().tm_mday
    day_in_week = now.timetuple().tm_wday
    ts_day = year % 1000 * 1000 + day_in_year
    ts_week = ts_day - day_in_week
    ts_month = ts_day - day_in_month
    