from ._anvil_designer import WorksTemplate
from anvil import *
from ...Cheteme.ElementsHtml.panels_works import create_panel, create_icon_panel_genres_en, create_icon_panel_bg_filter_list
from anvil.js.window import jQuery as jQ

n = 20
volume_filter = [{'bg':'100', 'filter':'100'},
               {'bg':'макс', 'filter':'999999'}]

time_filter = [{'bg':'Днес', 'filter':'d'},
               {'bg':'Седмица', 'filter':'w'},
               {'bg':'Месец', 'filter':'m'}]

engagement_filter = [{'bg':'Четени', 'filter':'l'},
               {'bg':'Харесвани', 'filter':'r'}]

class Works(WorksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)
    self.add_event_handler('show', self.show_form)

  def show_form(self, **event):
      
      summary = create_panel(target_id="#collection", n=n, engagement='p', summary=True)
      create_icon_panel_bg_filter_list(time_filter, "#period")
      create_icon_panel_bg_filter_list(engagement_filter, "#engagement")
      create_icon_panel_bg_filter_list(volume_filter, "#volume")
      create_icon_panel_genres_en(summary['types'], "#types")
      create_icon_panel_genres_en(summary['genres'], "#genres")
      
         
  def form_click(self, sender, **event):
     
     clicked = jQ(f'#{sender.id}')
     was_clicked = clicked.hasClass('filter')
     parent = clicked.parent()
     parent.children().removeClass('filter')

     if not was_clicked:
        clicked.toggleClass('filter')
     

     filter = {}
     wg = jQ('#genres').find('.filter')
     wt = jQ('#types').find('.filter')
     wp = jQ('#period').find('.filter')
     we = jQ('#engagement').find('.filter')
     wl = jQ('#volume').find('.filter')
     engagement = 'p'
     period = 'a'
     wn = n
     if wg:
        filter['wg'] = wg[0].id
     if wt:
        filter['wt'] = wt[0].id
     if wp:
        period = wp[0].id
        
     if we:
        engagement = we[0].id

     if wl:
        wn = int(wl[0].id)
     
     create_panel(filters=filter, target_id="#collection", n=wn, engagement=engagement, period=period, summary=False) 
     
     
     clicked_genre = jQ('#genres').find('.filter')
     #create_icon_panel_genres_en(summary['genres'], "#genres")
     if clicked_genre:
      id = clicked_genre[0].id
      jQ(f'#{id}').addClass('filter')
        
     
  
