import anvil.users
import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import hashlib
from time import time

def sha1_hash(data):
    string = data['title'] + str(time())
    sha1 = hashlib.sha1()
    sha1.update(string.encode('utf-8'))
    return sha1.hexdigest()

@anvil.server.callable
def work_publish(data):
    if data['wid'] == None:
      data['wid'] = sha1_hash(data)
    print(data)
    #app_tables.works.add_row()
      