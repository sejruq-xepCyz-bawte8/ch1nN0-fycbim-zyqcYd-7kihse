from ..Index import App
import anvil.http
import json





def api_engagement(wid:str, engagement:list, comment:str=None):
    #engagement:list -> open,read,like,comment,dislike,discoment
    data = {
        'target':'engagement',
        'device_id':App.DEVICE_ID,
        'secret':App.SECRET,
        'wid':wid,
        'engagement':engagement,
        'comment':comment
        }

    response = anvil.http.request(url="https://devices.chete.me",
                            method="POST",
                            data=json.dumps(data),
                            )
    resp_bytes = response.get_bytes()
    resp_text = resp_bytes.decode('utf-8')
    resp_json = json.loads(resp_text)
    return resp_json
