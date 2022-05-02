import requests
import json
import jsonpath
import pytest
import allure


# Pytest Fixtures
@pytest.fixture(scope="module")
def api_settingfunction():
    global api_url
    global api_url1
    global response
    api_url = "https://reqres.in/api/users/2"
    api_url1 = "https://httpbin.org/get"
    #response = requests.get(api_url)
    yield
    print("after functions")

"""
def test_postData(api_settingfunction):
    file = open('F:/Selenium/API_Pytest_Demo_Testing/data_files/Postdata.json', 'r')
    payload = json.loads(file.read())
    res = requests.post(api_url, payload)
    print(res.text)
    response_json = json.loads(res.text)
    created_at = jsonpath.jsonpath(response_json, "createdAt")
    id = jsonpath.jsonpath(response_json, 'id')
    job1 = jsonpath.jsonpath(response_json, 'job')

    print(created_at)
    print(id)
    print(job1)

    assert job1[0] == 'leader'
"""

# With Headers in the api
def test_postData(api_settingfunction):
    headers = {
        'H1' : 'Hello',
        'H2' : 'bye'
    }

    file = open('/data_files/Postdata.json', 'r')
    payload = json.loads(file.read())
    res = requests.post(api_url, payload, headers = headers)
    print(res.text)
    response_json = json.loads(res.text)
    created_at = jsonpath.jsonpath(response_json, "createdAt")
    id = jsonpath.jsonpath(response_json, 'id')
    job1 = jsonpath.jsonpath(response_json, 'job')

    print(res.headers)
    print(created_at)
    print(id)
    print(job1)

    assert job1[0] == 'leader'

def test_headers_provide(api_settingfunction):
    headers = {
        'h1' : 'first_name',
        'h2' : 'last_name'
        }
    response = requests.get(api_url1, headers= headers)
    print(response.text)

def test_url_with_params(api_settingfunction):
    params = {
        'name': 'Yogesh',
        'automation': 'python'
        }
    response = requests.get(api_url1, params= params)
    print(response.text)

def test_put_api_function():
    file = open("/data_files/Putdata.json", 'r')
    payload = json.loads(file.read())
    response = requests.put(api_url, payload)
    print(response.json())
    assert response.status_code == 200
    print("This is working")

def test_api_delete_function():
    res = requests.delete(api_url)
    print(res)
    assert res.status_code == 204

