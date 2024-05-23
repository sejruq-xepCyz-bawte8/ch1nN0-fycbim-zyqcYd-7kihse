
from .Template_Module import TemplateMemory

class Reader(TemplateMemory):
  def __init__(self, collection: object, data: list):
    super().__init__(loki_collection=collection)
    if data:
      self.collection.insert(data)

