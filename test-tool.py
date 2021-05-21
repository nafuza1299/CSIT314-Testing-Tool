import sys
import json
import utility
url = "https://csit314-testing-tool.herokuapp.com"
arguement = sys.argv

with open(arguement[1]) as f:
    data = json.load(f)
    x = 1
    for i in data:
        print("Test", x)

        if(i['type'].lower() == 'post'):
            post_req = utility.post_request(i['url'], i['body'], i['header'])
            check_url = i['check']['url'].replace('{{id}}', i['body']['contact']['id'])
            get_req = utility.get_request(check_url, i['header'])
            utility.request_assert(post_req.status_code, i['check']['success_code'])
            utility.request_assert(get_req.status_code, 200)

        elif(i['type'].lower() == 'get'):
           get_req = utility.get_request(i['url'], i['header'])
           utility.request_assert(get_req.status_code, i['check']['success_code'])

        elif (i['type'].lower() == 'delete'):
           del_req = utility.delete_request(i['url'], i['header'])
           utility.request_assert(del_req.status_code, i['check']['success_code'])

        x += 1

