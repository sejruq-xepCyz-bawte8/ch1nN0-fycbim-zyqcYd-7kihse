import anvil.server
import anvil.users
from anvil.tables import app_tables
import json
from CloudflareAuthors import cf_api
from Helpers import is_user_author, is_valid_uri, has_keys, hash_strings, has_record, status, fail
from time import time

AUTHORS = app_tables.authors
AUTHORS_DATA = app_tables.authorsdata
AUTHORS_HTML = app_tables.authorshtml
WORKS = app_tables.works

@anvil.server.callable
def get_author_id():
   user=anvil.users.get_user()
   if user and user['is_author'] and user['user_id']:
      user_id = user['user_id']
      author = AUTHORS.get(user_id=user_id)
      if author:
         user['author_id'] = author['author_id']
         return author['author_id']
      else:
         return None
   else:
      return None

@anvil.server.callable
def update_author_profile(html:str=None, data:dict=None):
   task = anvil.server.launch_background_task('update_author_profile_bg',
                                                html=html,
                                                data=data,
                                                user=anvil.users.get_user(),
                                                client = anvil.server.context.client.ip
                                                )
   return task    

      #client=anvil.server.context.client.ip


@anvil.server.background_task
def update_author_profile_bg(html:str=None, data:dict=None, user=None, client=None):
      print('Проверки на заявката')
      if not is_user_author(user=user, client=client): return False
      if not data or not html: return fail('Липсват метаданни или съдържание')
      data = parse_incoming_data(data)
      if not data : return False
      if not is_valid_uri(data["author_uri"]) : return False

      user_id = user['user_id']
      author_record = AUTHORS.get(user_id=user_id)

      if not author_record:
         author_uri=data["author_uri"]
         this_uri_records = AUTHORS.search(author_uri=author_uri)
         if len(this_uri_records) > 0 : return fail('Зает линк')
         print(f'Започва създаване на {data["author_uri"]}')
         result = new_profile(user_id=user_id, data=data, html=html)
      else:
         print(f'Започва ъпдейт на {data["author_uri"]}')
         result = update_profile(author_record=author_record, data=data, html=html)

      return result

def new_profile(user_id:str, data:dict, html:str)->dict:
   #new from incoming
   data_hash = hash_strings(json.dumps(data))
   html_hash = hash_strings(html)
   author_uri=data['author_uri']
   #new generated
   author_id=hash_strings(user_id, str(time()))
   #updates
   data['author_id'] = author_id
   #make records
   AUTHORS_DATA.add_row(**data)
   AUTHORS_HTML.add_row(author_id=author_id, html=html)
   new_author = AUTHORS.add_row(
      user_id=user_id,
      author_id=author_id,
      author_uri=author_uri,
      cf_success = False,
      data_hash=data_hash,
      html_hash=html_hash,
      version = 1,
      works = {}
    )
   
   
   data_public = parse_public_data_author(data=data, author_id=author_id, version=1, works={})
   cf_success = cf_api(data=data_public, html=html, target="author_profile")

   if cf_success:
      new_author.update(cf_success = True)
      return True
   else:
      return False
   


def update_profile(author_record, data:dict, html:str):
   #from incoming
   author_id:str = author_record['author_id']
   data_hash_new:str = hash_strings(json.dumps(data))
   html_hash_new:str = hash_strings(html)
   version:int = author_record['version'] + 1
   data_hash_old:str = author_record['data_hash']
   html_hash_old:str = author_record['html_hash']
   author_uri_new = data['author_uri']
   author_uri_old = author_record['author_uri']
   works = author_record['works']

   #checks
   if data_hash_new == data_hash_old and html_hash_new == html_hash_old:
      return fail('Нищо за ъпдейт')
   if author_uri_new != author_uri_old:
      this_uri_records = AUTHORS.search(author_uri=author_uri_new)
      if len(this_uri_records) > 0 : return fail('Зает линк')
   
   #updates
   data['author_id'] = author_id

   html_public = None
   if data_hash_new != data_hash_old:
       author_data_row = AUTHORS_DATA.get(author_id=author_id)
       author_data_row.update(data)
    
   if html_hash_new != html_hash_old:
        author_html_row = AUTHORS_HTML.get(author_id=author_id)
        author_html_row.update(html=html)
        html_public = html

   author_record.update(
      author_uri=author_uri_new,
      cf_success = False,
      data_hash=data_hash_new,
      html_hash=html_hash_new,
      version = version,
    )

   data_public = parse_public_data_author(data=data, author_id=author_id, version=version, works=works)
   print(f'Изпращане на заявката {data["author_uri"]}')
   cf_success = cf_api(data=data_public, html=html_public, target="author_profile")
   if cf_success:
      author_record.update(cf_success = True)
      return True
   else:
      return False
   


def parse_public_data_author(data:dict, author_id:str, version:int, works:dict)->dict:
  print('parse public data')
  pdata = {
     #from data
'author_name' : data['author_name'],
'background_image' : data['background_image'],
'author_uri' : data['author_uri'],
'description' : data['description'],
#from srv
'author_id' : author_id,
'version': version,
'works':works,
  }
  return pdata


def parse_incoming_data(data:dict):
   print('parse incoming to clean data')
   author_name:str = data.get('author_name') #:None,
   if not isinstance(author_name, str) or len(author_name) > 100 :
      print('No clean author_name', author_name)
      return False

   background_image:str = data.get('background_image') #:None,
   if background_image:
      if not background_image.startswith('data:image/') or len(background_image) > 1_000_000 :
         print('No clean data background_image', background_image)
         return False

   author_uri = data.get('author_uri') #:'',
   if not isinstance(author_uri, str) or len(author_uri) > 100 :
      print('No clean data author_uri', author_uri)
      return False
   description = data.get('description') #:'',
   if description:
      if not isinstance(description, str) or len(description) > 200 :
         print('No clean data description', description)
         return False

   clean_data = {
'author_name' : author_name,
'background_image' : background_image,
'author_uri' : author_uri,
'description' : description,
  }
 
   return clean_data