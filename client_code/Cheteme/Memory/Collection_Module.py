from anvil.js.window import chetemeDB

class Collection:
  def __init__(self):
    self.collection = chetemeDB.addCollection(self.__class__.__name__)

  def get_one(self, key, value):
    return self.collection.findOne({ key : value })