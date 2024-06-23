import anvil.http
import json

def api_publish_work(ticket:str, work_data:dict, work_html:str):
    data = {
        'target':'new_device',
        'device_id':False,
        'secret':'cheteme'
        }
    
    payload = json.dumps(data)

    headers= {
        "X-Cheteme-Target": "work",
        "X-Cheteme-Ticket": ticket,
                    }

    response = anvil.http.request(url="https://chete.me/?api=author",
                            method="POST",
                            data=payload,
                            headers=headers
                            )
    resp_bytes = response.get_bytes()
    resp_text = resp_bytes.decode('utf-8')
    resp_json = json.loads(resp_text)
    return resp_json