import json

import jsonpath
import requests

url= "https://reqres.in/api/users"
body = open('C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\CreateUser.json','r')
json_input = body.read()
request_body = json.loads(json_input)

response = requests.post(url,request_body)

print(response.content)
assert response.status_code == 201
print(response.headers.get("Content-Length"))

#Parse response in Json format
# response_json = json.loads(response.text)
response_body = jsonpath.jsonpath(response.json(),"id")
print(response_body[0])