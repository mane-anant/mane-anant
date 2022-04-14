import requests
import json
import jsonpath

def test_anant():
    url= "http://127.0.0.1/get/song"

    response= requests.get(url)
    print(response)

def test_anant1():
    json_response=json.loads(test_anant.response)
    pages = jsonpath.jsonpath(json_response,'id')
    assert pages[0] == 1