import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.tables.query as q
from time import time
import datetime

@anvil.server.background_task
def log_suspicious(cheteme:str, client):
     app_tables.suspicious.add_row(datetime=datetime.datetime.now(),
                                      type=client.type,
                                      ip=client.ip,
                                      location=client.location,
                                      cheteme=cheteme)