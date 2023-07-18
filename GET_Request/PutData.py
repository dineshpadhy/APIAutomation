import json
import jsonpath
import requests

url= "https://reqres.in/api/users/2"
body = open('C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\CreateUser.json','r')
json_input = body.read()
request_body = json.loads(json_input)

response = requests.put(url,request_body)
print(response.status_code)
assert response.status_code == 200
print(type(response))
response_body = json.loads(response.text)
print(type(response_body))
print(response_body["updatedAt"])
update_time = jsonpath.jsonpath(response_body,"updatedAt")
print(update_time[0])