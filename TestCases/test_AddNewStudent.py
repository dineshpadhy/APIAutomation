import jsonpath
import requests
import json

def test_add_student_data():
    global id
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\RequestJson.json",'r')
    request_body = json.loads(f.read())
    response = requests.post(API_URL,request_body)
    print(response.text)
    id = jsonpath.jsonpath(json.loads(response.text),"id")
    print(id[0])

def test_update_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    f = open("C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\UpdateRequestJson.json",'r')
    request_body = json.loads(f.read())
    response = requests.put(API_URL,request_body)
    print(response.text)

def test_get_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    # response_data=json.loads(response.text)
    response_data = response.json()
    id_response = jsonpath.jsonpath(response_data,"data.id")
    print(response.text)
    assert id_response[0] == id[0]

def test_delete_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.delete(API_URL)
    print(response.text)

