import anvil.server
import anvil.users
from anvil.tables import app_tables
import anvil.http
import json
from datetime import datetime, time



WORKS_NEW = app_tables.worksnew
CHETEME = anvil.secrets.get_secret("CHETEME")
API_URL = "https://api.chete.me/"

@anvil.server.background_task
def today_new_works():
    key = 'today'
    today_unix = today()
    data_iterator = WORKS_NEW.search()
    today_works = [{w['wid']:w['ptime']} for w in data_iterator if w['ptime'] > today_unix]
    print(today_works)
    status('пейлод ...')
    payload = prepare_payload(data=today_works, key=key)
    status('изпраща апи заявка ...')
    result = parse_request(payload=payload)
    print(result)



def prepare_payload(data:dict, key:str):
    request_data = {
       'CHETEME': CHETEME,
       'target': 'registry',
       'data':data,
       'key':key
       }
    payload = json.dumps(request_data)
    return payload

def status(message):
   anvil.server.task_state['message'] = message


def parse_request(payload:str):
    try:
        response = anvil.http.request(url=API_URL,
                                    method="POST",
                                    data=payload,
                                    )
        status('има апи отговор ...')
    except anvil.http.HttpError as e:
        print('API HttpError', e)
        status(f'API HttpError {e}')
        return False

    body_bytes = response.get_bytes()
    body_string = body_bytes.decode('utf-8')

    try:
        rdata = json.loads(body_string)
        if not rdata:
            print('responce not rdata')
            status(f'Неправилен отговор от сървъра')
            return False
    except:
        print('responce json err')
        return False

    success = rdata.get('success')
    if success:
        status(f'Успешен отговор от API сървъра')
        return True
    else:
        status(f'API сървъра съобщава за неуспех {rdata.get("message")}')
    return False


def today():
    now = datetime.now()
    midnight_today = datetime.combine(now.date(), time.min)
    unix_timestamp = int(midnight_today.timestamp())
    return unix_timestamp