import utility
import generate_request
'''
Unit tests for utility.py.
'''

# test put request using asdf as id. changes values to first=nice last=one
def test_request_assert():
   res = utility.request_assert(200, 200)
   assert res == None

#assert content assert with put request to user jack
def test_content_assert():
    data ={'contact': {'first': 'string', 'last': 'string'}}
    header = {'Content-Type': 'application/json', 'Authorization': 'ae34g1ce'}
    put_req = generate_request.put_request("https://csit314-testing-tool.herokuapp.com/contacts/jack", data, header)

    res = utility.content_assert({'contact': {'first': 'string', 'last': 'string'}}, put_req )
    assert res == None

# test generate pass msg using num 1
def test_generate_pass_msg():
    assert utility.generate_pass_msg(1) == "Test 1 passed"

# test generate pass msg using num 1
def test_generate_error_msg():
    try:
        raise AssertionError("test error")
    except AssertionError as e:
        error = e

    assert utility.generate_error_msg(1, error) == "Test 1 test error"
test_content_assert()
