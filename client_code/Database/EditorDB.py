from anvil_extras.storage import indexed_db
from anvil_extras import non_blocking
from time import time
from random import randint
import datetime

AUTHOR_ID = 'author_id'

WORK_TEMPLATE = {
  'title':None,
  'genres':[None,None,None,None],
  'keywords':[],
  'icons':[],
  'background-image':None,
  'font':'Adys',
  'background-color':'#FFFFFF',
  'color':'#000000',
  'cover_mask':50,
  'mask_color':'#FFFFFF',
  'words':0,
  'ctime':0,
  'mtime':0,
  'published':False,
  'author_id':AUTHOR_ID,
  'work_id':None,
  'work_uri':'',
  'id_local': True,
  'id_server':False,
  'size': 0
}

class EditorClass:
   def __init__(self) -> None:
      #stores and templates
      self.template:dict = WORK_TEMPLATE
      self.store_data = indexed_db.create_store('editor_meta')
      self.store_html = indexed_db.create_store('editor_html')
      #current
      self.data = None
      self.html = None
   
   #itterators
   def all_works_data(self):
      try:
        iterator = self.store_data.values()
      except:
        iterator = []
      return iterator
     
   def all_works_id(self):
      try:
        iterator = self.store_html.keys()
      except:
        iterator = []
      return iterator

   def new_work(self, html:str=None, title:str=None)->str:
      #work id
      work_id = f"{time():.10f}{randint(1000000000, 9999999999)}"
      #data store
      data = self.template
      data['work_id'] = work_id
      if title:
         data['title'] = title
      else:
         now = datetime.datetime.now()
         data['title'] = now.strftime("%d-%b-%Y %H:%M")
      data['ctime'] = data['mtime'] = time()
      item_data = {work_id:data}
      
      #html
      if not html: html = ''
      item_html = {work_id:html}

      self.store_data.update(item_data)
      self.store_html.update(item_html)
      #result
      return work_id


   def set_current(self, work_id:str)->bool:
      self.data = self.store_data[work_id]
      self.html = self.store_html[work_id]
      return True


   def update(self, full:bool=True):
      work_id = self.data['work_id']
      self.data['mtime'] = time()
      self.store_data[work_id] = self.data
      if full:
         self.store_html[work_id] = self.html
      return True

      
   def delete_by_id(self, work_id:str):
      self.store_data.pop(work_id)
      self.store_html.pop(work_id)
      return True
      



    