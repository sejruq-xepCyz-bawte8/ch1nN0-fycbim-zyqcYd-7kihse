from anvil_extras.storage import indexed_db
from anvil.js.window import loki

class Memory:
  def __init__(self):
    self.db = loki('cheteme.db')
   
    self.published = self.db.addCollection('published')
    self.likes = self.db.addCollection('likes')
    self.reads = self.db.addCollection('reads')
    self.genres = self.db.addCollection('genres')