import json
import random
from faker import Faker
fake = Faker()
url = "https://csit314-testing-tool.herokuapp.com/contacts/sq0cq"

# {
#         "url":"https://csit314-testing-tool.herokuapp.com/contacts",
#         "type":"POST",
#         "header" :{
#             "Content-Type":"application/json",
#             "Authorization":"ae34g1ce"
#         },
#         "body":{
#             "contact":{
#                 "id":"int",
#                 "first":"string",
#                 "last":"string"
#             }
#         },
#         "check":{
#             "url":"https://csit314-testing-tool.herokuapp.com/contacts/{{id}}",
#             "success_code":"201"
#         }
#     }
for _ in range(10):
    id = random.randint()
    my_dict = {
        'url': "https://csit314-testing-tool.herokuapp.com",
        "type": "POST",
        "header" :{
            "Content-Type" : "application/json"
        },
        'body': {
            'contact':{
                'id': id,
                'first': fake.name(),
                'last': fake.name()
            }
        },
        "check":{
            "url": "https://csit314-testing-tool.herokuapp.com/contacts/"+str(id),
            "success_code": "201"
        }
    }

    print(my_dict)