from ..Index import App
import anvil.http
import json



def api_today():
    request_data = prepare_request(target='today', target_id='today')
    response = make_request(request_data)
    data, _ = parse_response(response)
    return data


def api_work(target_id='beach'):
    request_data = prepare_request(target='work', target_id=target_id)
    response = make_request(request_data)
    data, html = parse_response(response)
    return data, html


def api_author(target_id='beach'):
    request_data = prepare_request(target='author', target_id=target_id)
    response = make_request(request_data)
    data, html = parse_response(response)
    return data, html



def prepare_request(target=None, target_id=None):
    if not target and not target_id and not App.IS_DEVICE and not App.DEVICE_ID:
        return None
    data = {
        'target':target,
        'target_id':target_id,
        'device_id':App.DEVICE_ID
    }
    return data

def make_request(data):
    if not data:
        return None
    try:
        response = anvil.http.request(url="https://pub.chete.me",
                        method="POST",
                        data=json.dumps(data),
                        )
    except:
        return None
    return response

def parse_response(response):
    if not response: return None, None
    resp_bytes = response.get_bytes()
    resp_text = resp_bytes.decode('utf-8')
    resp_json = json.loads(resp_text)
    data_string = resp_json['data']
    if data_string:
        data = json.loads(data_string)
    else:
        data = None
    html = resp_json['html']
    return data, html