from ._anvil_designer import WorksTemplate
from anvil import *
from ...Cheteme.ElementsHtml.panels_module import create_panel, create_icon_panel
from anvil.js.window import jQuery as jQ

class Works(WorksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from ...Cheteme.Main import navigation_click
    self.navigation_click = navigation_click
    self.init_components(**properties)
    self.add_event_handler('show', self.show_form)

  def show_form(self, **event):
      n = 11
      summary = create_panel(target_id="#collection", n=n, engagement='p', summary=True)
      
      create_icon_panel(summary['types'], "#types")
      create_icon_panel(summary['genres'], "#genres")
         
  def form_click(self, sender, **event):
     n = 11
     clicked = jQ(f'#{sender.id}')
     was_clicked = clicked.hasClass('filter')
     parent = clicked.parent()
     parent.children().removeClass('filter')
     if not was_clicked:
        clicked.toggleClass('filter')
     filter_elements = jQ('#filters').find('.filter')
     filter = {}
     wg = jQ('#genres').find('.filter')
     wt = jQ('#types').find('.filter')
     
     if wg:
        filter['wg'] = wg[0].id
     if wt:
        filter['wt'] = wt[0].id

     create_panel(filters=filter, target_id="#collection", n=n, engagement='p', summary=False) 
     
     print(filter)
