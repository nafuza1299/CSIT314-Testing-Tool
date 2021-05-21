import pytest
import requests
import json

#get request
url = "https://csit314-testing-tool.herokuapp.com/contacts"
res = requests.get(url)
get_Content = json.loads(res.content)['contacts']
print(get_Content)
#post request
data = {
  "contact":
    {
        "id": "tseter",
        "first": "Test",
        "last": "Test2"
    }
}
x = requests.post(url, data = data)
print(x)
