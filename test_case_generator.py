import case_generator
import json

#test result from delete generate dict using post request, contact and id
def test_delete_generation():
    data = {
        "url": "https://csit314-testing-tool.herokuapp.com/contacts",
        "type": "POST",
        "header": {
            "Content-Type": "application/json",
            "Authorization": "ae34g1ce"
        },
        "body": {
            "contact": {
                "id": 999,
                "first": "FFEeoeGynvucKklsPuwM",
                "last": "fdTZqbsAuNFOymGMGFKC"
            }
        },
        "check": {
            "url": "https://csit314-testing-tool.herokuapp.com/contacts/821",
            "success_code": "201"
        }
    }
    res = case_generator.delete_generate(data, 'contact', 'id')
    answer = {'url': 'https://csit314-testing-tool.herokuapp.com/contacts/999', 'type': 'DELETE', 'header': {'Authorization': 'ae34g1ce'}, 'check': {'url': 'https://csit314-testing-tool.herokuapp.com/contacts/999', 'success_code': '200'}}
    assert json.dumps(res) == json.dumps(answer)
    assert res == answer


#test result from put generate dict using post request, contact and id
def test_put_generation():
    data = {
        "url": "https://csit314-testing-tool.herokuapp.com/contacts",
        "type": "POST",
        "header": {
            "Content-Type": "application/json",
            "Authorization": "ae34g1ce"
        },
        "body": {
            "contact": {
                "id": 999,
                "first": "FFEeoeGynvucKklsPuwM",
                "last": "fdTZqbsAuNFOymGMGFKC"
            }
        },
        "check": {
            "url": "https://csit314-testing-tool.herokuapp.com/contacts/821",
            "success_code": "201"
        }
    }
    res = case_generator.put_generate(data, 'contact', 'id')
    answer = {'url': 'https://csit314-testing-tool.herokuapp.com/contacts/999', 'type': 'PUT', 'header': {'Content-Type': 'application/json', 'Authorization': 'ae34g1ce'}, 'body': {'contact': {'first': 'FFEeoeGynvucKklsPuwM', 'last': 'fdTZqbsAuNFOymGMGFKC'}}, 'check': {'url': 'https://csit314-testing-tool.herokuapp.com/contacts/999', 'success_code': '200'}}
    assert json.dumps(res) == json.dumps(answer)
    assert res == answer
    
#assert dictionary key of post generation, as post generates random value
def test_post_generation():
    data = {
        "url": "https://csit314-testing-tool.herokuapp.com/contacts",
        "type": "POST",
        "header": {
            "Content-Type": "application/json",
            "Authorization": "ae34g1ce"
        },
        "body": {
            "contact": {
                "id": "int",
                "first": "string",
                "last": "string"
            }
        },
        "check": {
            "url": "https://csit314-testing-tool.herokuapp.com/contacts/821",
            "success_code": "201"
        }
    }
    res = case_generator.post_generate(data, 'contact', 'id')
    answer = {'url': 'https://csit314-testing-tool.herokuapp.com/contacts', 'type': 'POST', 'header': {'Content-Type': 'application/json', 'Authorization': 'ae34g1ce'}, 'body': {'contact': {'id': 8784, 'first': 'QwNUJiicGY WiqYOdOpYT', 'last': 'plbLkSpZJqBwqpnzVmtE'}}, 'check': {'url': 'https://csit314-testing-tool.herokuapp.com/contacts/8784', 'success_code': '200'}}
    assert res.keys() == answer.keys()
