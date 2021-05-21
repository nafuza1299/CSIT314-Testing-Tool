import pytest
import requests
import json


def get_request(url, headers):
    #get request
    res = requests.get(url, headers = headers)
    get_Content = json.loads(res.content)
    print("GET REQUEST: ", res)
    print("GET CONTENT: ", get_Content)

#post request
def post_request(url, data, headers):
    body = json.dumps(data)
    res = requests.post(url, headers = headers ,  data = body)
    get_Content = json.loads(res.content)
    print("POST REQUEST: ", res)
    print("POST CONTENT: ", get_Content)


