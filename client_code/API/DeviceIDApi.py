import anvil.http
import json

def api_new_device():
    data = {
        'target':'new_device',
        'device_id':False,
        'secret':'cheteme'
        }

    response = anvil.http.request(url="https://chete.me/?api=device",
                            method="POST",
                            data=json.dumps(data),
                            )
    resp_bytes = response.get_bytes()
    resp_text = resp_bytes.decode('utf-8')
    resp_json = json.loads(resp_text)
    return resp_json
