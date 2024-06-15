import anvil.server
import anvil.users
from anvil.tables import app_tables
import json
from time import time
import hashlib


WORKS = app_tables.works
PROFILES = app_tables.authorprofiles

from CloudflareAuthors import cf_author_work, cf_author_profile
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
    status('Проверки на заявката')
    if not is_user_author(user=user, client=client): return False

    author_record = PROFILES.get(user_id=user["user_id"])
    if not author_record : return fail('Първо направете профил :)')

    if not data or not html: return fail('Липсват метаданни или съдържание')
    if not has_keys(target=data, keys=['work_uri', 'work_id', 'title', 'ptime']) : return False
    if not is_valid_uri(data["work_uri"]) : return False
    
    this_uri_records = WORKS.search(work_uri=data["work_uri"], user_id=user["user_id"])
    for u in this_uri_records:
        if u["work_id"] != data["work_id"]: return fail('Ползвате линка в друга творба')

    
    old_record = WORKS.get(user_id=user["user_id"], work_id=data["work_id"])

    if old_record:
        status(f'Започва ъпдейт на {data["title"]}')
        result_work = update_work(old_record=old_record, data=data, html=html)
        result_profile = update_profile_works(user["user_id"])
    else:
        status(f'Започва публикуване на {data["title"]}')
        author_id = author_record['author_id']
        result_work =  publish_new_work(user_id=user["user_id"], author_id=author_id, data=data, html=html)
        result_profile = update_profile_works(user["user_id"])

    if result_work and result_profile:
       status('ГОТОВО :) всичко е успешно')
       return True
    else:
       status('ГОТОВО :( имаше проблеми и резултата е несигурен.')
       return False
       

def publish_new_work(user_id:str, author_id:str, data:dict, html:str):
    wid=hash_strings(user_id, data["work_id"])
    data_text=json.dumps(data)
    data["version"] = 1
    data['author_id'] = author_id
    data['published'] = True
    record_hash = hash_strings(data_text, html)
    cf_success = cf_author_work(data=data, html=html, wid=wid)
    if cf_success:
        WORKS.add_row(user_id=user_id,
                      author_id = author_id,
                      work_id=data["work_id"],
                      work_uri=data["work_uri"],
                      wid=wid,
                      published = True,
                      cf_success = cf_success,
                      data=json.dumps(data),
                      html=html,
                      hash=record_hash,
                      version = 1)
    
    else:
      return False
   
    if has_record(WORKS, record_hash):
      status(f'Творбата е публикувана, следва ъпдейт на профила с нея')
      return True
    else:
      return fail('Неуспешен бекъп')
 

def update_work(old_record, data:str, html:str):
    data_text=json.dumps(data)
    data["version"] = old_record["version"] + 1
    data['author_id'] = old_record["author_id"]
    data['published'] = True
    record_hash = hash_strings(data_text, html)
    cf_success = cf_author_work(data=data, html=html, wid=old_record["wid"])
    if cf_success:
        old_record.update(work_uri=data["work_uri"],
                        cf_success = cf_success,
                        data=json.dumps(data),
                        html=html,
                        hash=record_hash,
                        version = data["version"])
    
    else:
      return False
   
    if has_record(WORKS, record_hash):
      status(f'Творбата е публикувана, следва ъпдейт на профила с нея')
      return True
    else:
      return fail('Неуспешен бекъп')




def update_profile_works(user_id:str):
    status('Започва ъпдейт на профила')
    published_works = WORKS.search(user_id=user_id, published=True)
    author_works = {}
    status('Ъпдейт на списъка творби на профила')
    for w in published_works:
        print(w)
        author_works[w["work_uri"]] = w["wid"]

    old_record = PROFILES.get(user_id=user_id)
    
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