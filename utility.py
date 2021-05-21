import pytest
import requests
import json

# get request
def get_request(url, headers):
    res = requests.get(url, headers = headers)
    get_Content = json.loads(res.content)
    print("GET REQUEST: ", res.status_code)
    print("GET CONTENT: ", get_Content)
    return res

#post request
def post_request(url, data, headers):
    body = json.dumps(data)
    res = requests.post(url, headers = headers ,  data = body)
    get_Content = json.loads(res.content)
    print("POST REQUEST: ", res.status_code)
    print("POST CONTENT: ", get_Content)
    return res

# delete request
def delete_request(url, headers):
    res = requests.delete(url, headers = headers)
    print("DELETE REQUEST: ", res.status_code)
    return res

#assert code
def request_assert(res, code):
    assert int(res) == int(code)
