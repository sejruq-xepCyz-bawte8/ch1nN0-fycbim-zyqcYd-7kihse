import anvil.server
import anvil.users
from anvil.tables import app_tables
import json
from time import time
import hashlib


WORKS = app_tables.works
WORKS_DATA = app_tables.worksdata
WORKS_HTML = app_tables.workshtml
PROFILES = app_tables.authorprofiles
AUTHORS = app_tables.authors
AUTHORS_DATA = app_tables.authorsdata
AUTHORS_HTML = app_tables.authorshtml
WORKS_NEW = app_tables.worksnew

from CloudflareAuthors import cf_api
from Helpers import is_user_author, is_valid_uri, has_keys, hash_strings, has_record, status, fail


@anvil.server.callable
def publish_author_work(html:str=None, data:dict=None):
    task = anvil.server.launch_background_task('publish_author_work_bg',
                                               html=html,
                                               data=data,
                                               user=anvil.users.get_user(),
                                               client=anvil.server.context.client.ip)
    return task


@anvil.server.background_task
def publish_author_work_bg(html:str=None, data:dict=None, user=None, client=None):
    print('Проверка на валидност потр/автор')
    if not is_user_author(user=user, client=client): return False

    author_record = AUTHORS.get(user_id=user["user_id"])

    if not author_record : return fail('Първо направете профил :)')

    if not data or not html: return fail('Липсват метаданни или съдържание')

    data = parse_incoming_data(data)
    if not data : return fail('Грешни метаданни')

    if not is_valid_uri(data["work_uri"]) : return fail('Грешен пермалинк')

    author_id = author_record.get('author_id')
    
    if data["work_uri"] in author_record['works'] : return fail('Ползвате линка в друга творба')
 
    work_record = WORKS.get(author_id=user["author_id"], work_id=data["work_id"])

    if work_record:
        result_work = update_work(work_record=work_record, author_record=author_record, data=data, html=html)
        
    else:
        print(f'Започва публикуване на {data["title"]}')
        result_work =  new_work(author_record=author_record, data=data, html=html)
        

    if result_work:
       status('ГОТОВО :) всичко е успешно')
       return True
    else:
       status('ГОТОВО :( имаше проблеми и резултата е несигурен.')
       return False
       

def parse_incoming_data(data:dict):
   print('parse incoming to clean data')
   title:str = data.get('title') #:None,
   if not isinstance(title, str) or len(title) > 100 :
      print('No clean data title', title)
      return False
   genres = data.get('genres') #:[None,None,None,None],
   if not isinstance(genres, list) or len(genres) > 5 :
      print('No clean data genres', genres)
      return False
   keywords = data.get('keywords') #:[],
   if not isinstance(keywords, list) or len(keywords) > 20 :
      print('No clean data keywords', keywords)
      return False
   icons = data.get('icons') #:[],
   if not isinstance(icons, list) or len(icons) > 5 :
      print('No clean data icons', icons)
      return False
   background_image:str = data.get('background_image') #:None,
   if background_image:
      if not background_image.startswith('data:image/') or len(background_image) > 1_000_000 :
         print('No clean data background_image', background_image)
         return False
   font:str = data.get('font') #:'Adys',
   if not isinstance(font, str) or len(font) > 50 :
      print('No clean data font', font)
      return False
   background_color:str = data.get('background_color') #:'#FFFFFF',
   if not isinstance(background_color, str) or len(background_color) > 10 :
      print('No clean data background_color', background_color)
      return False
   color = data.get('color') #:'#000000',
   if not isinstance(color, str) or len(color) > 10 :
      print('No clean data color', color)
      return False
   cover_mask = data.get('cover_mask') #:50,
   if not isinstance(cover_mask, str) or len(cover_mask) > 3 :
      print('No clean data cover_mask', cover_mask)
      return False
   mask_color = data.get('mask_color') #:'#FFFFFF',
   if not isinstance(mask_color, str) or len(mask_color) > 10 :
      print('No clean data mask_color', mask_color)
      return False
   words = data.get('words') #:0,
   if not isinstance(words, int) or words > 1_000_000 :
      print('No clean data words', words)
      return False
   ctime = data.get('ctime') #:0,
   if not isinstance(ctime, (int, float)) or ctime < 1_710_000_000 or ctime > time():
      print('No clean data ctime', ctime)
      return False
   mtime = data.get('mtime') #:0,
   if not isinstance(mtime, (int, float)) or mtime < 1_710_000_000 or mtime > time() :
      print('No clean data mtime', mtime)
      return False
   work_id = data.get('work_id') #:None,
   if not isinstance(work_id, str) or len(work_id) > 40 :
      print('No clean data work_id', work_id)
      return False
   work_uri = data.get('work_uri') #:'',
   if not isinstance(work_uri, str) or len(work_uri) > 100 :
      print('No clean data work_uri', work_uri)
      return False
   size = data.get('size') #: 0
   if not isinstance(size, int) or size > 10_000_000 :
      print('No clean data size', size)
      return False

   clean_data = {
'title' : title,
'genres' : genres,
'keywords' : keywords,
'icons' : icons,
'background_image' : background_image,
'font' : font,
'background_color' : background_color,
'color' : color,
'cover_mask' : cover_mask,
'mask_color' : mask_color,
'words' : words,
'ctime' : ctime,
'mtime' : mtime,
'work_id' : work_id,
'work_uri' : work_uri,
'size' : size,
  }
   print('parse incoming data passed')
   return clean_data

def parse_public_data_work(data:dict, wid:str, author_id:str, ptime:float, version:int)->dict:
  print('parse public data')
  pdata = {
     #from data
'title' : data['title'],
'genres' : data['genres'],
'keywords' : data['keywords'],
'icons' : data['icons'],
'background_image' : data['background_image'],
'font' : data['font'],
'background_color' : data['background_color'],
'color' : data['color'],
'cover_mask' : data['cover_mask'],
'mask_color' : data['mask_color'],
'words' : data['words'],
'work_uri' : data['work_uri'],
'size' : data['size'],
#from srv
'wid' : wid,
'author_id' : author_id,
'ptime': ptime,
'version': version,
  }
  print('parse public data passed')
  return pdata

def new_work(author_record, data:dict, html:str):
      #from incoming
      author_id:str = author_record['author_id']
      work_id:str = data["work_id"]
      work_uri:str = data['work_uri']
      #new 
      wid:str = hash_strings(author_id, work_id)
      ptime:float = time()
      version:int = 1
      data_hash:str = hash_strings(json.dumps(data))
      html_hash:str = hash_strings(html)
    
      #update dict
      data['wid'] = wid

      #save work to db
      WORKS_DATA.add_row(**data)
      WORKS_HTML.add_row(wid=wid, html=html)
      work_record = WORKS.add_row(
         author_id = author_id,
         wid=wid,
         work_id = work_id,
         work_uri=work_uri,
         cf_work = False,
         cf_author = False,
         published = True,
         data_hash=data_hash,
         html_hash = html_hash,
         version = version,
         ptime = ptime,
    )

      #update author db
      works:dict = author_record['works']
      works[work_uri] = wid
      author_version:int = author_record['version'] + 1
      author_record.update(works = works, version = author_version)

      # update work public/online version  now
      data_work_public = parse_public_data_work(data=data, wid=wid, author_id=author_id, ptime=ptime, version=version)
      cf_work = cf_api(data=data_work_public, html=html, target="author_work")
      cf_author = update_profile_works(author_record)
      # update author profile

      #check for success
      if cf_work and cf_author:
         work_record.update(cf_work = True, cf_author = True)
         return True
      elif cf_work and not cf_author:
         work_record.update(cf_work = True, cf_author = False)
         return False
      elif not cf_work and cf_author:
         work_record.update(cf_work = False, cf_author = True)
         return False
      else:
         work_record.update(cf_work = False, cf_author = False)
         return False




def update_work(work_record, author_record, data:str, html:str):
   #from incoming
   work_uri_new:str = data['work_uri']
   data_hash_new:str = hash_strings(json.dumps(data))
   html_hash_new:str = hash_strings(html)
   #from record and upd
   author_id:str = author_record['author_id']
   work_id:str = work_record["work_id"]
   work_uri_old:str = work_record["work_uri"]
   wid:str = work_record['wid']
   ptime:float = work_record['ptime']
   version:int = work_record['version'] + 1
   data_hash_old:str = work_record['data_hash']
   html_hash_old:str = work_record['html_hash']

   #update work records
   if data_hash_old != data_hash_new:
       work_data_record = WORKS_DATA.get(wid=wid)
       work_data_record.update(data)
    
   if html_hash_old != html_hash_new:
        work_html_record = WORKS_HTML.get(wid=wid)
        work_html_record.update(html=html)

   work_record.update(
       cf_work = False,
       cf_author = False,
       published = True,
       data_hash=data_hash_new,
       html_hash=html_hash_new,
       version = version,
       work_uri = work_uri_new,
    )
   
   #update author db
   if work_uri_new != work_uri_old:
      works:dict = author_record['works']
      works[work_uri_new] = wid
      if works and work_uri_old in works:
         del works[work_uri_old]
      else:
         works = {work_uri_new:wid}
      author_version:int = author_record['version'] + 1
      author_record.update(works = works, version = author_version)

   #update online
   data_public = parse_public_data_work(data=data, wid=wid, author_id=author_id, ptime=ptime, version=version)
   cf_work = cf_api(data=data_public, html=html, target="author_work")
   if work_uri_new != work_uri_old:
      cf_author = update_profile_works(author_record)
   else:
      cf_author = True

   #check for success
   if cf_work and cf_author:
      work_record.update(cf_work = True, cf_author = True)
      return True
   elif cf_work and not cf_author:
      work_record.update(cf_work = True, cf_author = False)
      return False
   elif not cf_work and cf_author:
      work_record.update(cf_work = False, cf_author = True)
      return False
   else:
      work_record.update(cf_work = False, cf_author = False)
      return False

def update_profile_works(author_record):
   #author record is already updated from work and will run only if neceseary
   #from incoming
   author_id:str = author_record['author_id']
   version:int = author_record['version']
   works:dict = author_record['works']
   data = AUTHORS_DATA.get(author_id=author_id)
   #generate data
   

   data_public = parse_public_data_author(data=data, author_id=author_id, version=version, works=works)
   print(f'Изпращане на заявката {data["author_uri"]}')
   cf_success = cf_api(data=data_public, html=None, target="author_profile_works")
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