import json
import pytest
import jsonpath
import requests

url= "https://reqres.in/api/users"

@pytest.fixture()
def file_open():
    global body
    print("Before testcase")
    body = open('C:\\Users\\dines\\PycharmProjects\\APIAutomation\\resources\\CreateUser.json','r')
    yield
    print("after testcase")
    body.close()

# @pytest.mark.skip("this is not valid for current build")
@pytest.mark.Smoke
def test_create_new_user(file_open):
    json_input = body.read()
    request_body = json.loads(json_input)
    response = requests.post(url,request_body)
    print(response.content)
    assert response.status_code == 201
    print(response.headers.get("Content-Length"))
    response_json = json.loads(response.text)
    response_body = jsonpath.jsonpath(response_json,"id")
    print(response_body[0])

@pytest.mark.Sanity
def test_create_other_user(file_open):
    json_input = body.read()
    request_body = json.loads(json_input)
    response = requests.post(url,request_body)
    print(response.headers.get("Content-Length"))
    response_json = json.loads(response.text)
    response_body = jsonpath.jsonpath(response_json,"id")
    print(response_body[0])