import anvil.http
import json

def api_image(id:str):
    data = {
        'target':'new_device',
        'device_id':False,
        'secret':'cheteme'
        }

    response = anvil.http.request(url=f"https://chete.me/?api=image&id={id}",
                            method="POST",
                            #data=json.dumps(data),
                            )
    resp_bytes = response.get_bytes()
    resp_text = resp_bytes.decode('utf-8')
    #resp_json = json.loads(resp_text)
    return resp_text
