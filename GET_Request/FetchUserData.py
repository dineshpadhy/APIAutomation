import requests
import json
import jsonpath
url= "https://reqres.in/api/users?page=2"

response = requests.get(url)
# # print(response.content)
# # print(response.headers)
# print(response.status_code)
# assert response.status_code ==200
# print(response.headers.get("date"))
# print(response.headers.get("server"))
#
# print(response.cookies)
# print(response.encoding)
# #time taken by sending the request and getting the response
# print(response.elapsed)

json_response = json.loads(response.text)
pages = jsonpath.jsonpath(json_response,"total_pages")
assert pages[0] ==2

for i in range(0,3):
    first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name[0])