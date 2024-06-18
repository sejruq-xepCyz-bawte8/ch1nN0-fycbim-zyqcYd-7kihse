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
WORKS_NEW = app_tables.worksnew

from CloudflareAuthors import cf_api, cf_author_profile
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
    print('Проверки на заявката')
    if not is_user_author(user=user, client=client): return False

    author_record = PROFILES.get(user_id=user["user_id"])
    if not author_record : return fail('Първо направете профил :)')

    if not data or not html: return fail('Липсват метаданни или съдържание')
   
    if not is_valid_uri(data["work_uri"]) : return False

    author_id = author_record.get('author_id')
    
    this_uri_records = WORKS.search(work_uri=data["work_uri"], author_id=user["author_id"])
    for u in this_uri_records:
        if u["work_id"] != data["work_id"]: return fail('Ползвате линка в друга творба')

    
    old_record = WORKS.get(author_id=user["author_id"], work_id=data["work_id"])

    if old_record:
        print(f'Започва ъпдейт на {data["title"]}')
        result_work = update_work(old_record=old_record, data=data, html=html)
        result_profile = update_profile_works(user["user_id"])
    else:
        print(f'Започва публикуване на {data["title"]}')
        result_work =  publish_new_work(author_id=author_id, data=data, html=html)
        result_profile = update_profile_works(author_id)

    if result_work and result_profile:
       status('ГОТОВО :) всичко е успешно')
       return True
    else:
       status('ГОТОВО :( имаше проблеми и резултата е несигурен.')
       return False
       



def parse_incoming_data(data:dict):
  
  title:str = data.get('title') #:None,
  if not isinstance(title, str) or len(title) > 100 : return False
  genres = data.get('genres') #:[None,None,None,None],
  if not isinstance(genres, list) or len(genres) > 5 : return False
  keywords = data.get('keywords') #:[],
  if not isinstance(keywords, list) or len(keywords) > 20 : return False
  icons = data.get('icons') #:[],
  if not isinstance(icons, list) or len(icons) > 5 : return False
  background_image:str = data.get('background_image') #:None,
  if background_image:
     if not background_image.startswith('data:image/') or len(background_image) > 1_000_000 : return False
  font:str = data.get('font') #:'Adys',
  if not isinstance(font, str) or len(font) > 50 : return False
  background_color:str = data.get('background_color') #:'#FFFFFF',
  if not isinstance(background_color, str) or len(background_color) > 10 : return False
  color = data.get('color') #:'#000000',
  if not isinstance(color, str) or len(color) > 10 : return False
  cover_mask = data.get('cover_mask') #:50,
  if not isinstance(cover_mask, int) or len(cover_mask) > 100 : return False
  mask_color = data.get('mask_color') #:'#FFFFFF',
  if not isinstance(mask_color, str) or len(mask_color) > 10 : return False
  words = data.get('words') #:0,
  if not isinstance(words, int) or len(words) > 1_000_000 : return False
  ctime = data.get('ctime') #:0,
  if not isinstance(ctime, (int, float)) or ctime < 1_710_000_000 or ctime > time(): return False
  mtime = data.get('mtime') #:0,
  if not isinstance(mtime, (int, float)) or mtime < 1_710_000_000 or mtime > time() : return False
  work_id = data.get('work_id') #:None,
  if not isinstance(work_id, str) or len(work_id) > 40 : return False
  work_uri = data.get('work_uri') #:'',
  if not isinstance(work_uri, str) or len(work_uri) > 100 : return False
  size = data.get('size') #: 0
  if not isinstance(size, int) or len(size) > 10_000_000 : return False

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
 
  return clean_data

def parse_public_data_work(data:dict, wid:str, author_id:str, ptime:float, version:int)->dict:
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
  return pdata

def publish_new_work(author_id:str, data:dict, html:str):
      data_clean = parse_incoming_data(data)
      if not data_clean : return False

      wid=hash_strings(author_id, data_clean["work_id"])
      ptime = time()
      version = 1
    
      data_hash = hash_strings(json.dumps(data_clean))
      html_hash = hash_strings(html)
    
      data_clean['wid'] = wid

      data_public = parse_public_data_work(data=data_clean, wid=wid, author_id=author_id, ptime=ptime, version=version)
      print('new work1')
      WORKS_DATA.add_row(**data_clean)
      WORKS_HTML.add_row(wid=wid, html=html)
      new_work = WORKS.add_row(
         author_id = author_id,
         wid=wid,
         cf_success = False,
         published = True,
         data_hash=data_hash,
         html_hash = html_hash,
         version = version,
         ptime = ptime,
    )

      cf_success = cf_api(data=data_public, html=html, target="author_work")

      if cf_success:
         new_work.update(cf_success = True)
         return True
      else:
         return False




def update_work(old_record, data:str, html:str):
    data_clean = parse_incoming_data(data)
    if not data_clean : return False

    data_hash = hash_strings(json.dumps(data_clean))
    html_hash = hash_strings(html)

    version = old_record['version'] + 1
    wid = old_record['wid']
    author_id = old_record['author_id']
    ptime = old_record['ptime']
    
    data_clean['wid'] = wid
    data_public = parse_public_data_work(data=data_clean, wid=wid, author_id=author_id, ptime=ptime, version=version)
    
    if data_hash != old_record['data_hash']:
       work_data_row = WORKS_DATA.get(wid=wid)
       work_data_row.update(data_clean)
    
    if html_hash != old_record['html_hash']:
        work_html_row = WORKS_HTML.get(wid=wid)
        work_html_row.update(html=html)

    old_record.update(
       cf_success = False,
       published = True,
       data_hash=data_hash,
       html_hash=html_hash,
       version = version,
    )

    cf_success = cf_api(data=data_public, html=html, target="author_work")

    if cf_success:
       old_record.update(cf_success = True)
       return True
    else:
       return False








def update_profile_works(author_id:str):
    status('Започва ъпдейт на профила')
    published_works = WORKS.search(author_id=author_id, published=True)
    author_works = {}
    status('Ъпдейт на списъка творби на профила')
    for w in published_works:
        author_works[w["work_uri"]] = w["wid"]

    old_record = PROFILES.get(author_id=author_id)
    
    data = json.loads(old_record["data"])
    html = old_record["html"]
    data["works"] = author_works
    # after having data and html modified
    status(f'Приготвяне на заявката на {data["author_uri"]}')
    data_text=json.dumps(data)
    data["version"] = old_record["version"] + 1
    record_hash = hash_strings(data_text, html)
    status(f'Изпращане на заявката {data["author_uri"]}')

    cf_success = cf_author_profile(data=data, html=html)
    if cf_success:
        old_record.update(author_uri=data["author_uri"],
                           data=json.dumps(data),
                           html=html,
                           works = author_works,
                           cf_success=cf_success,
                           hash=record_hash,
                           version=data["version"])
    else:
      return False
   
    if has_record(PROFILES, record_hash):
      status(f'Готово')
      return True
    else:
      return fail('Неуспешен бекъп на профиля')