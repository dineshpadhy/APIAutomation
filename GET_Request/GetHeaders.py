import requests
header_data = {'T1':'K1','T2':'K2'}
response = requests.get("https://httpbin.org/get", headers=header_data)
print(response.text)

