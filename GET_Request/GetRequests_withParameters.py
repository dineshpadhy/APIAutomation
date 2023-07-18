import requests
param = {'T1':'K1','T2':'K2'}
response = requests.get("https://httpbin.org/get", params=param)
print(response.text)