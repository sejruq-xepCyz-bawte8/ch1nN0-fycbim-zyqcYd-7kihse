import anvil.http

def test():
    url = "https://cheteme-read.bqbhhcj5mp.workers.dev/"
    response = anvil.http.request(url, json=True)
    print(f"Response DICT: {dict(response)}")
    print("RESPONSE:", response)