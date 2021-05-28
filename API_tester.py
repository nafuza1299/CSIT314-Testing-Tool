import sys
import json
import utility
import generate_request

'''
Tool used to test API based on specified JSON.
Can be called from cli with jsonfile as parameter.

'''

def testing_tool(jsonfile = "output.json"):

    # variable used to store failed and passed messages
    results_list = []

    # open json file to be tested
    with open(jsonfile) as f:
        data = json.load(f)
        x = 1
        for i in data:
            print("Test", x) #counter
            
            # post request case
            if(i['type'].lower() == 'post'):

                # send post request
                post_req = generate_request.post_request(i['url'], i['body'], i['header'])
                # check_url = i['check']['url'].replace('{{id}}', i['body']['contact']['id'])
                get_req = generate_request.get_request(i['check']['url'], i['header'])

                # assert for response code and content
                try:
                    utility.request_assert(post_req.status_code, i['check']['success_code'])
                    utility.request_assert(get_req.status_code, 200)
                    utility.content_assert(i['body'], get_req)
                    results_list.append(utility.generate_pass_msg(x))
                    
                except Exception as e:
                    results_list.append(utility.generate_error_msg(x, e))

            # get request case
            elif(i['type'].lower() == 'get'):
                # send get request
                get_req = generate_request.get_request(i['url'], i['header'])

                # assert for response code
                try:
                    utility.request_assert(get_req.status_code, i['check']['success_code'])
                    results_list.append(utility.generate_pass_msg(x))
                    
                except Exception as e:
                    results_list.append(utility.generate_error_msg(x, e))

            # delete request case
            elif (i['type'].lower() == 'delete'):
                #send delete request
                del_req = generate_request.delete_request(i['url'], i['header'])
                get_req = generate_request.get_request(i['check']['url'], i['header'])

                try:
                    #assert for response code
                    utility.request_assert(del_req.status_code, i['check']['success_code'])
                    utility.request_assert(get_req.status_code, 404)
                    results_list.append(utility.generate_pass_msg(x))
                    
                except AssertionError as e:
                    results_list.append(utility.generate_error_msg(x, e))
                
            # put request case
            elif (i['type'].lower() == 'put'):
                # send put request
                put_req = generate_request.put_request(i['url'], i['body'], i['header'])
                get_req = generate_request.get_request(i['check']['url'], i['header'])

                
                try:
                    #assert for response code and content
                    utility.request_assert(put_req.status_code, i['check']['success_code'])
                    utility.request_assert(get_req.status_code, 200)
                    utility.content_assert(i['body'], get_req)
                    results_list.append(utility.generate_pass_msg(x))
                    
                except Exception as e:
                    results_list.append(utility.generate_error_msg(x,e))
                
            x += 1

    print("\nTest Summary:")
    for i in results_list:
        print(i)

# allows tool to function in cli by passing jsonfile argument
if len(sys.argv) > 1:
    testing_tool(sys.argv[1])
