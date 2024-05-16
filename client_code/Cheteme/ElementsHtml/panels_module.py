from anvil.js.window import jQuery as jQ
from ...Cheteme.Memory import works, content, genres
from ...Cheteme.ElementsHtml import CoverClass
from ...Cheteme.ElementsHtml.generic import HtmlElement
from ...Cheteme.ElementsHtml.Icon import Icon



def create_panel(filters=None, target_id:str="#collection", engagement:str='l', period:str='a', n=5, chart:bool=False, summary:bool = False):
    
    all_works, aditional = works.get_last(filters=filters, engagement=engagement, period=period, n=n)
    
    append_cards(all_works, target_id=target_id)
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
    
def append_cards(works, target_id, chart=False):
    jQ(target_id).empty()
    i = 0
    for work in works:
      i += 1
      work_content = content.get_one(key='wid', value=work['w'])
      if work_content and 'data' in work_content:
        work_data = work_content['data']
        cover = CoverClass(work_data).el
        if chart:
          special = HtmlElement(text=i, css='ch-cover-chartid')()
          jQ(cover).append(special)  
        jQ(target_id).append(cover)






def create_icon_panel(icons, target_id):
   
   jQ(target_id).empty()
   for i in icons:
      
      awesome = genres.get_one(key="gid", value=i)
      
      if awesome:
        icon = Icon(bg=awesome['bg'], id=i)
        icon.el.attr('onclick', "formClick(this, event)")

        if icon:
          jQ(target_id).append(icon.el)
      else:
         print('bgnone')