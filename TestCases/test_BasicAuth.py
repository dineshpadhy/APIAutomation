import jsonpath
import requests
from requests.auth import HTTPBasicAuth

def test_basicAuth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('dinesh', 'password'))
    print(response.json())
