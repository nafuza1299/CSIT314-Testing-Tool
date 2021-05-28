import json, requests

# generate a get request using url and headers. returns the response
def get_request(url, headers):
    res = requests.get(url, headers = headers)
    print("GET REQUEST: ", res.status_code)
    if(res.status_code == 200):
        get_Content = json.loads(res.content)
        print("GET CONTENT: ", get_Content)
    return res

# generate a post request using url and headers. returns the response
def post_request(url, data, headers):
    body = json.dumps(data)
    res = requests.post(url, headers = headers ,  data = body)
    print("POST REQUEST: ", res.status_code)
    if(res.status_code == 201):
        get_Content = json.loads(res.content)
        print("POST CONTENT: ", get_Content)
    return res

# generate a delete request using url and headers. returns the response
def delete_request(url, headers):
    res = requests.delete(url, headers = headers)
    print("DELETE REQUEST: ", res.status_code)
    return res

# generate a put request using url and headers. returns the response
def put_request(url, data, headers):
    body = json.dumps(data)
    res = requests.put(url, headers = headers, data = body)
    get_Content = json.loads(res.content)
    print("PUT REQUEST: ", res.status_code)
    print("PUT CONTENT: ", get_Content)
    return res