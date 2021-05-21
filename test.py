import utility
import json

# Unit tests that uses asdf and jack as id

# Test get request function using jack as id
def test_get_request():
    res = utility.get_request('https://csit314-testing-tool.herokuapp.com/contacts/jack', {'Authorization' : 'ae34g1ce'})
    answer = {'contact': {'id': 'jack', 'first': 'Jack', 'last': 'Bauer', 'avatar': 'http://oyster.ignimgs.com/wordpress/stg.ign.com/2014/04/6-01-JackChange.jpg'}}
    
    assert json.loads(res.content) == answer
    assert res.json() == answer
    assert res.status_code == 200

# test post request using values: id=test first=yes last=wow
def test_post_request():
    res = utility.post_request('https://csit314-testing-tool.herokuapp.com/contacts', {"contact":{"id":"asdf","first":"yes","last":"wow"}}, {'Content-Type': 'application/json', 'Authorization' : 'ae34g1ce'})
    answer = {'contact': {'id': 'asdf', 'first': 'yes', 'last': 'wow'}}
    
    assert json.loads(res.content) == answer
    assert res.json() == answer
    assert res.status_code == 201

    # try again to get code 409 (resource already found error)
    res2 = utility.post_request('https://csit314-testing-tool.herokuapp.com/contacts', {"contact":{"id":"asdf","first":"yes","last":"wow"}}, {'Content-Type': 'application/json', 'Authorization' : 'ae34g1ce'})
    assert res2.status_code == 409

# test put request using asdf as id. changes values to first=nice last=one
def test_put_request():
    res = utility.put_request("https://csit314-testing-tool.herokuapp.com/contacts/asdf", {"contact":{"first":"nice","last":"one"}}, {'Content-Type': 'application/json', 'Authorization' : 'ae34g1ce'})
    answer = {'contact': {'id': 'asdf', 'first': 'nice', 'last': 'one'}}
    
    assert json.loads(res.content) == answer
    assert res.json() == answer
    assert res.status_code == 200

# test delete request using asdf as id. uses get request to check if deleted
def test_delete_request():
    res = utility.delete_request("https://csit314-testing-tool.herokuapp.com/contacts/asdf", {'Authorization' : 'ae34g1ce'})
    assert res.status_code == 200

    res2 = utility.get_request('https://csit314-testing-tool.herokuapp.com/contacts/asdf', {'Authorization' : 'ae34g1ce'})
    assert res2.status_code == 404


# test_post_request()
# test_put_request()
# test_delete_request()
