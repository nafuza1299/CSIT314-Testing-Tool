import sys
import json
import utility
url = "https://csit314-testing-tool.herokuapp.com"
arguement = sys.argv


with open(arguement[1]) as f:
    data = json.load(f)
    for i in data:
       if(i['type'].lower() == 'post'):
            utility.post_request(i['url'], i['body'], i['header'])
            check_url = i['check']['url'].replace('{{id}}', i['body']['contact']['id'])
            utility.get_request(check_url, i['header'])
       elif(i['type'].lower() == 'get'):
           utility.get_request(i['url'], i['header'])


