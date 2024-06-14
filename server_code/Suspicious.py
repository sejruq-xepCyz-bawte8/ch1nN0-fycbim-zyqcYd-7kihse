from anvil.tables import app_tables
import datetime


def log_suspicious(cheteme:str, client):
     app_tables.suspicious.add_row(datetime=datetime.datetime.now(),
                                      type=client.type,
                                      ip=client.ip,
                                      location=client.location,
                                      cheteme=cheteme)