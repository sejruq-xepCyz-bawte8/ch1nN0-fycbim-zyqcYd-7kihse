import anvil.server
import anvil.users
from anvil.tables import app_tables
import json
from CloudflareAuthors import cf_author_profile
from Helpers import is_user_author, is_valid_uri, has_keys, hash_strings, has_record, status, fail



PROFILES = app_tables.authorprofiles


@anvil.server.callable
def update_author_profile(html:str=None, data:dict=None):
    task = anvil.server.launch_background_task('update_author_profile_bg',
                                               html=html,
                                               data=data,
                                               user=anvil.users.get_user(),
                                               client=anvil.server.context.client.ip)
    return task    



@anvil.server.background_task
def update_author_profile_bg(html:str=None, data:dict=None, user=None, client=None):
      
      status('Проверки на заявката')
      if not is_user_author(user=user, client=client): return False
      return 42
      if not data or not html: return fail('Липсват метаданни или съдържание')
      keys_to_check = ['author_uri', 'author_name']
      if not has_keys(target=data, keys=keys_to_check) : return False
      if not is_valid_uri(data["author_uri"]) : return False
      
      this_uri_records = PROFILES.search(author_uri=data["author_uri"])
      for u in this_uri_records:
         if u["user_id"] != user["user_id"]: return fail('Зает линк')
      
      
      old_record = PROFILES.get(user_id=user["user_id"])

      if not old_record:
        
        status(f'Започва създаване на {data["author_uri"]}')
        result = make_new_profile(user_id=user["user_id"], data=data, html=html)
      else:
        status(f'Започва ъпдейт на {data["author_uri"]}')
        result = update_profile(old_record=old_record, data=data, html=html)

      if result:
         status('ГОТОВО всичко е успешно')
         return True
      else:
         status('ПРИКЛЮЧИ но с грешки')
         return False
      return result

def make_new_profile(user_id:str, data:dict, html:str)->dict:
   data_text=json.dumps(data)
   data["version"] = 1
   record_hash = hash_strings(data_text, html)
   cf_success = cf_author_profile(data=data, html=html)
   if cf_success:
      PROFILES.add_row(user_id=user_id,
                                       author_uri=data["author_uri"],
                                       data=data_text,
                                       html=html,
                                       cf_success=cf_success,
                                       hash=record_hash,
                                       version=1)
   else:
      return False
   
   if has_record(PROFILES, record_hash):
      status('Бекъпа е записан')
      return True
   else:
      return fail('Неуспешен бекъп')

def update_profile(old_record, data:dict, html:str):
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
                           cf_success=cf_success,
                           hash=record_hash,
                           version=data["version"])
   else:
      return False
   
   if has_record(PROFILES, record_hash):
      status('Бекъпа е записан')
      return True
   else:
      return fail('Неуспешен бекъп')



