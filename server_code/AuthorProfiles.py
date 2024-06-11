import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
import anvil.server
import anvil.tables.query as q
import anvil.secrets

CHETEME = anvil.secrets.get_secret("CHETEME")

@anvil.server.callable
def update_author_profile(html, data):
    print('server publ')
    user = anvil.users.get_user()
    if user['is_author']:
      print('server publ save/upd')
      user_id = user['user_id']
      old_record = app_tables.authorprofiles.get(user_id=user_id)
      author_uri = data['author_uri']
      if not old_record:
        # making new need look for uri first
        check_uri_all = len(app_tables.authorprofiles.search(author_uri=author_uri))
        if check_uri_all == 0:
          app_tables.authorprofiles.add_row(user_id=user_id, author_uri=author_uri, data=json.dumps(data), html=html)
        else:
          return {'success':False, 'message':'duplicate_uri'}
      else:
        if author_uri == old_record['author_uri']:
          data_string = json.dumps(data)
          old_record.update(author_uri=author_uri, data=data_string, html=html)
          cf = cloudflare_api(data)
          return cf
        else:
          check_uri_all = len(app_tables.authorprofiles.search(author_uri=author_uri))
          if check_uri_all == 0:
            data_string = json.dumps(data)
            old_record.update(author_uri=author_uri, data=data_string, html=html)
            cf = cloudflare_api(data)
            return cf
          else:
            return {'success':False, 'message':'duplicate_uri'}


def cloudflare_api(data):
  data['CHETEME'] = CHETEME
  data_string = json.dumps(data)
  cf = anvil.http.request(url="https://api.chete.me/author",
                    method="POST",
                    data=data_string,
                    )