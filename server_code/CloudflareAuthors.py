import anvil.secrets
import anvil.http
import json
import anvil.server

CHETEME = anvil.secrets.get_secret("CHETEME")
API_URL = "https://api.chete.me/"


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
    except anvil.http.HttpError as e:
        print('API HttpError', e)
        anvil.server.task_state(f'API HttpError {e}')
        return False

    body_bytes = response.get_bytes()
    body_string = body_bytes.decode('utf-8')

    try:
        rdata = json.loads(body_string)
        if not rdata:
            print('responce not rdata')
            anvil.server.task_state(f'Неправилен отговор от сървъра')
            return False
    except:
        print('responce json err')
        return False

    success = rdata.get('success')
    if success:
        anvil.server.task_state(f'Успешен отговор от API сървъра')
        return True
    else:
        anvil.server.task_state(f'API сървъра съобщава за неуспех {rdata.get('message')}')
    return False


def cf_api(data:dict, html:str, target:str):
  payload = prepare_payload(data=data, html=html, target=target)
  result = parse_request(payload=payload)
  return result

def cf_author_profile(data:dict, html:str):
   return cf_api(data=data, html=html, target="author_profile")

def cf_author_work(data:dict, html:str, wid:str):
   pdata = public_data_work(data=data, wid=wid)
   return cf_api(data=pdata, html=html, target="author_work")




def public_data_work(data:dict, wid:str)->dict:
    pdata = {}
    keys = ['title',
            'genres',
            'keywords',
            'icons',
            'background-image',
            'font',
            'background-color',
            'color',
            'cover_mask',
            'mask_color',
            'ptime',
            'work_uri']
    for key in keys:
        pdata[key] = data.get(key)
    pdata['wid'] = wid
    return pdata