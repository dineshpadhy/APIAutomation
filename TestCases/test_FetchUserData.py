import requests
import json
import jsonpath
import pytest
@pytest.mark.Smoke
def test_fetch_userdata():
    url= "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    pages = jsonpath.jsonpath(json_response,"total_pages")
    assert pages[0] ==2
    for i in range(0,3):
        first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
        print(first_name[0])