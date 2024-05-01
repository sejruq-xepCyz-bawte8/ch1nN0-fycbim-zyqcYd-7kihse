from anvil_extras.storage import indexed_db
from anvil.js.window import chDB, chDBadapter
from time import sleep




class Memory:
  def __init__(self):
    self.db = chDB
    self.adapter = chDBadapter
    self.published = self.db.addCollection('published')
    self.likes = self.db.addCollection('likes')
    self.reads = self.db.addCollection('reads')
    self.genres = self.db.addCollection('genres')
    self.works = self.db.addCollection('works')
    self.test = self.db.addCollection('test' , {'unique': ['test']})
    

  def load_data(self, data: dict = {}, collection: str = 'test'):
    for d in data:
      r = getattr(self, collection).findOne({'test': d['test'] })
      print('r', r, d['test'])
      if not r:
        getattr(self, collection).insert(d)
      else:
        r['data'] = d['data']
        getattr(self, collection).update(r)
   
    
    #avaivable = self.adapter.checkAvailability()
    #print('avaivable', avaivable)
    #self.db.saveDatabase(res)
    

  def count_records(self, collection: str = 'test'):
    result = getattr(self, collection).chain().find().count()
    return result

def res(result):
  print('result', result)

if __name__ == "__main__":
  
  m = Memory()
  
  m.load_data([{'test':"hello", 'data':'1' },{'test':"hello2", 'data':'2' },{'test':"hello", 'data':'3' },{'test':"hello2", 'data':'4' }, ])
  r = m.count_records()

  print(r)