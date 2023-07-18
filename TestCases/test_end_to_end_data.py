import jsonpath
import requests
import json

def test_add_new_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\RequestJson.json",'r')
    request_body = json.loads(f.read())
    response = requests.post(API_URL,request_body)
    id = jsonpath.jsonpath(response.json(),"id")
    print(id[0])

    tech_URL = "https://thetestingworldapi.com/api/technicalskills"
    f = open("C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\technicalSkills.json", 'r')
    request_body = json.loads(f.read())
    request_body['id'] = int(id[0])
    request_body['st_id'] = id[0]
    response = requests.post(tech_URL, request_body)
    print(response.text)

    addr_URL = "https://thetestingworldapi.com/api/addresses"
    f = open("C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\addressJson.json", 'r')
    request_body = json.loads(f.read())
    request_body['stId'] = id[0]
    response = requests.post(addr_URL,request_body)
    print(response.text)

    finalStudent_URL = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(finalStudent_URL)
    print(response.text)


