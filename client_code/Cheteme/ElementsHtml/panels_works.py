from anvil.js.window import jQuery as jQ
from ..Memory import works, content, genres
from . import CoverClass
from .Icon import Icon



def create_panel(filters=None, target_id:str="#collection", engagement:str='l', period:str='a', n=5, chart:bool=False, summary:bool = False):
    jQ(target_id).empty()
    all_works, aditional = works.get_last(filters=filters, engagement=engagement, period=period, n=n)
    
    append_cards(all_works, target_id=target_id, chart=True)
    if len(aditional) > 0:
      append_cards(aditional, target_id=target_id, chart=False)

    if summary:
       genres = {w['wg'] for w in all_works if 'wg' in w}
       genres_additional = {w['wg'] for w in aditional if 'wg' in w}

       types = {w['wt'] for w in all_works if 'wt' in w}
       types_additional = {w['wt'] for w in aditional if 'wt' in w}

       summary_result = {
          'genres' : genres | genres_additional,
          'types': types | types_additional,
       }
       return summary_result
    
def append_cards(works, target_id, chart:bool=False):
    print('works', len(works), 'chart',chart)
    
    i = 0
    for work in works:
      i += 1
      work_content = content.get_one(key='wid', value=work['w'])
      if work_content and 'data' in work_content:
        work_data = work_content['data']
        work_data['header'] = i
        cover = CoverClass(work_data)
        if chart:
          cover.css_add_class('is_chart')
        else:
          cover.css_add_class('no_chart')
        jQ(target_id).append(cover())


def create_icon_panel_genres_en(icons, target_id):
   jQ(target_id).empty()
   for i in icons:
      aw = genres.get_one(key="gid", value=i)
      if aw:
        icon = Icon(bg=aw['bg'], id=i)
        icon.el.attr('onclick', "formClick(this, event)")
        if icon:
          jQ(target_id).append(icon.el)
      else:
         print('bgnone')

def create_icon_panel_bg_filter_list(icons, target_id):
   if icons:
    for i in icons:
        icon = Icon(bg=i['bg'], id=i['filter'])
        icon.el.attr('onclick', "formClick(this, event)")
        if icon:
            jQ(target_id).append(icon.el)
        else:
          print('bgnone')