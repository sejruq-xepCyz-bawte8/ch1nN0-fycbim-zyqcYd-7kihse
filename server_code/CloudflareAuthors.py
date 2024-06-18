import anvil.secrets
import anvil.http
import json
import anvil.server

CHETEME = anvil.secrets.get_secret("CHETEME")
API_URL = "https://api.chete.me/"

def status(message):
   anvil.server.task_state['message'] = message

def prepare_payload(data:dict, html:str, target:str):
    request_data = {
       'CHETEME': CHETEME,
       'target': target,
       'data':data,
       'html':html
       }
    payload = json.dumps(request_data)
    return payload

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


def cf_api(data:dict, html:str, target:str):
  status('пейлод ...')
  payload = prepare_payload(data=data, html=html, target=target)
  status('изпраща апи заявка ...')
  result = parse_request(payload=payload)
  return result



