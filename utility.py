import requests
import json

#get request
def get_request(url, headers):
    res = requests.get(url, headers = headers)
    print("GET REQUEST: ", res.status_code)
    if(res.status_code == 200):
        get_Content = json.loads(res.content)
        print("GET CONTENT: ", get_Content)
    return res

#post request
def post_request(url, data, headers):
    body = json.dumps(data)
    res = requests.post(url, headers = headers ,  data = body)
    print("POST REQUEST: ", res.status_code)
    if(res.status_code == 201):
        get_Content = json.loads(res.content)
        print("POST CONTENT: ", get_Content)
    return res

#delete request
def delete_request(url, headers):
    res = requests.delete(url, headers = headers)
    print("DELETE REQUEST: ", res.status_code)
    return res

#put request
def put_request(url, data, headers):
    body = json.dumps(data)
    res = requests.put(url, headers = headers, data = body)
    get_Content = json.loads(res.content)
    print("PUT REQUEST: ", res.status_code)
    print("PUT CONTENT: ", get_Content)
    return res

#assert code
def request_assert(res, code):
    try:
        assert int(res) == int(code)
    except:
        raise AssertionError("Status Code Error: " + str(res) + " " + str(code))
    

#assert content
def content_assert(input, output):
    #load output content
    get_Content = json.loads(output.content)

    #loop through the content body
    try:
        for key in input:
            output = get_Content[key]
            input = input[key]
            for i in input:
                input_data = input[i]
                output_data = output[i]
                assert str(input_data) == str(output_data)
    except:
        raise AssertionError("Content Error: \n" + str(input) + "\nAnd\n" + str(output))

def generate_pass_msg(num):
    return "Test " + str(num) + " passed"

def generate_error_msg(num, error):
    return "Test " + str(num) + " " + str(error)
