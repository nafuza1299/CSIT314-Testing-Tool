import sys
import json
import utility
url = "https://csit314-testing-tool.herokuapp.com"
arguement = sys.argv


with open(arguement[1]) as f:
    data = json.load(f)
    for i in data:
        utility.get_request(i['url'])