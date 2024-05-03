from ._anvil_designer import NewTemplate
from anvil import *
from ...Cheteme.ElementsHtml.Icon import Icon
from anvil_extras import ChipsInput

class New(NewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.upload_cover = FileLoader(text="")
    self.cover = Image(width=20, height=20)


    # Any code you write here will run before the form opens.

  def genre_change(self, **event_args):
    print(self.genre.selected)
    if not self.genre.selected:
      self.genre.items = ['1','2','3']
    else:
      if self.genre.selected[0] == '1':
        self.genre.items = ['1','11','13','14']
      elif self.genre.selected[0] == '2':
        self.genre.items = ['2','211','213','214']
      else:
        pass
    pass


