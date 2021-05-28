import sys
import json
import utility

def testing_tool(jsonfile = "output.json"):

    # variable used to store which one failed and passed
    results_list = []

    with open(jsonfile) as f:
        data = json.load(f)
        x = 1
        for i in data:
            print("Test", x) #counter
            #if post request
            if(i['type'].lower() == 'post'):
                # if 'count' in i:
                #     count = int(i['count'])
                # else:
                    # count = 1
                # for x in range(0, count):

                #send post request
                post_req = utility.post_request(i['url'], i['body'], i['header'])
                # check_url = i['check']['url'].replace('{{id}}', i['body']['contact']['id'])
                get_req = utility.get_request(i['check']['url'], i['header'])

                #assert for response code and content
                utility.request_assert(post_req.status_code, i['check']['success_code'])
                utility.request_assert(get_req.status_code, 200)
                utility.content_assert(i['body'], get_req)

            elif(i['type'].lower() == 'get'):
                #send get request
                get_req = utility.get_request(i['url'], i['header'])

                #assert for response code
                utility.request_assert(get_req.status_code, i['check']['success_code'])

            elif (i['type'].lower() == 'delete'):
                #send delete request
                print(i)
                del_req = utility.delete_request(i['url'], i['header'])
                print(del_req)

                #assert for response code
                utility.request_assert(del_req.status_code, i['check']['success_code'])

            elif (i['type'].lower() == 'put'):
                # send put request
                put_req = utility.put_request(i['url'], i['body'], i['header'])
                get_req = utility.get_request(i['check']['url'], i['header'])

                #assert for response code and content
                utility.request_assert(put_req.status_code, i['check']['success_code'])
                utility.request_assert(get_req.status_code, 200)
                utility.content_assert(i['body'], get_req)
            x += 1

if len(sys.argv) > 1:
    testing_tool(sys.argv[1])