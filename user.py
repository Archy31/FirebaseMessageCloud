
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

data = {
    'message': 0
}

respo = requests.post("http://127.0.0.1:8000/api", json=data)

print(respo.text)