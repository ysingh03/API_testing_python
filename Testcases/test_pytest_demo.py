import pytest
import requests
import json
import jsonpath

# Pytest Fixtures
@pytest.fixture(scope="module")
def SettingUp_Environment():
    global api_url
    global response
    api_url = "https://reqres.in/api/users?page=2"
    response = requests.get(api_url)
    yield
    print(response.text)
    print(response.status_code)

a = 9

@pytest.mark.skipif(a > 10, reason= "function is for linux not for others")
def test_verify_status_code(SettingUp_Environment):
    assert response.status_code == 200
    '''
    for failing the test case 
    assert response.status_code == 201 
    '''


def test_verify_id_value(SettingUp_Environment):
    json_res = json.loads(response.text)
    id = jsonpath.jsonpath(json_res, 'data[0].id')
    assert id == [7]
