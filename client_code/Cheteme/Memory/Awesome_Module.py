
from .Template_Module import TemplateMemory

class Awesome(TemplateMemory):
  def __init__(self, collection: object, data: list):
    super().__init__(loki_collection=collection)
    if data:
      self.collection.insert(data)

  def get_icon_code(self, bg: str):
    icon = self.get_one('bg', bg)
    if icon :
      return icon['name']
    else:
      return 'icons'

  def get_icon_bg(self, name: str):
    return self.get_one('name', name)