import pytest
import requests
import json


def get_request(url):
    #get request
    res = requests.get(url)
    get_Content = json.loads(res.content)['contacts']
    print(get_Content)

#post request
def post_request(url, data):
    x = requests.post(url, data = data)
    print(x)
