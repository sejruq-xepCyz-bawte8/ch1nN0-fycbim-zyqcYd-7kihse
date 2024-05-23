
class TemplateMemory:
  def __init__(self, loki_collection: object):
    self.collection = loki_collection

  def load_data(self, data: list):
    self.collection.insert(data)

  def get_all(self):
    return self.collection.chain().find().data({'removeMeta':True})

  def get_one(self, key, value):
    return self.collection.findOne({ key : value })


  def get_objects(self, key: str, value):
      return self.collection.chain().find({ key : value }).data({'removeMeta':True})
  
  def get_list(self, key: str, value):
      obj_list = self.collection.chain().find({ key : value }).data({'removeMeta':True})
      list_items = [next(iter(proxy)) for proxy in obj_list]
      return list_items
      #return [x for x in obj_list].

  def get_column(self, column: str, key: str = None, value = None):
      if key:
        obj_list = self.collection.chain().find({ key : value }).data({'removeMeta':True})
      else:
        obj_list = self.collection.chain().find().data({'removeMeta':True})
      print('getcol', column, key, value)
      return [x[column] for x in obj_list]

  def get_list_between_values(self, column: str, key: str, value1 = int, value2 = int):
      obj_list = self.collection.chain().find({ key : { '$between': [value1, value2] }}).data({'removeMeta':True})
      
      return [x for x in obj_list]


  def get_column_between_values(self, column: str, key: str, value1 = int, value2 = int):
      obj_list = self.collection.chain().find({ key : { '$between': [value1, value2] }}).data({'removeMeta':True})
      
      return [x[column] for x in obj_list]

  def get_list_between_keys(self, key_min: str, key_max: str, value = int):
      obj_list = self.collection.chain().find({ key_min : { '$lte': value}}).find({ key_max : { '$gte': value}}).data({'removeMeta':True})

      return [x for x in obj_list]


  def get_column_between_keys(self, column: str, key_min: str, key_max: str, value = int):
      obj_list = self.collection.chain().find({ key_min : { '$lte': value}}).find({ key_max : { '$gte': value}}).data({'removeMeta':True})
      
      return [x[column] for x in obj_list]