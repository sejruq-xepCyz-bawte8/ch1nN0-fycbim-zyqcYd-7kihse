import anvil.http

def read_api():
    response = anvil.http.request("https://client-info.bqbhhcj5mp.workers.dev/", json=True)
    print(response) 


def read_api_data(data:dict = None):
    data = {"id":None, 'cors-secret':'your-cors-secret'}
    response = anvil.http.request(url="https://id-worker.bqbhhcj5mp.workers.dev/",
                    method="POST",
                    data=data,
                    json=True
                    ) 
    #print(f"Response MIME type: {response.content_type}")
    print(response) 