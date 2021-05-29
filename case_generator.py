import json
from faker import Faker
fake = Faker()

'''
Tool used to generate random parameters and test cases from specified JSON.
Outputs the JSON into output.json.

'''

# input dictionary values for posting
def post_generate(i, body_key, id):
    # template for posting
    dict_post = {
        "url": None,
        "type": "POST",
        "header": {
            None
        },
        "body": {

        },
        "check": {
            "url": None,
            "success_code": "200"
        }
    }

    dict_post['body'][body_key] = {}
    dict_post["url"] = i['url']

    #generate random value for post body
    for x in i['body'][body_key]:
        if (i['body'][body_key][x] == "int"):
            dict_post['body'][body_key][x] = fake.pyint()
        if (i['body'][body_key][x] == "string"):
            dict_post['body'][body_key][x] = fake.pystr()

    dict_post["check"]["url"] = i['url'] + "/" + str(dict_post['body'][body_key][id])
    dict_post["header"] = i["header"]
    return dict_post

# input dictionary values for deletion
def delete_generate(i, body_key, id):
    # template for deletion
    dict_delete =   {
        "url": None,
        "type":"DELETE",
        "header" :{
            None
        },
        "check":{
            "url": None,
            "success_code":"201"
        }
    }

    dict_delete["url"] =  i['url'] + "/" + str(i['body'][body_key][id])
    dict_delete["check"]["url"] =  i['url'] + "/" + str(i['body'][body_key][id])

    #generate random value for put body
    for x in i["header"]:
        if(x != "Content-Type"):
            dict_header = {x: i['header'][x]}
            dict_delete['header'] = dict_header
    return dict_delete

# input dictionary values for updating
def put_generate(i, body_key, id):
    
    #template for updating
    dict_put = {
        "url": None,
        "type": "PUT",
        "header": {
            None
        },
        "body": {

        },
        "check": {
            "url": None,
            "success_code": "200"
        }
    }

    dict_put['body'][body_key] = {}
    dict_put["url"] = i['url'] + "/" + str(i['body'][body_key][id])
    dict_put["check"]["url"] = i['url'] + "/" + str(i['body'][body_key][id])
    for x in i['body'][body_key]:
        if (x != id):
            dict_put['body'][body_key][x] = i['body'][body_key][x]
    dict_put["header"] = i["header"]
    return dict_put

# main function for generating test cases
def run_generation(json_file,  id = None, del_option = 0, put_option = 0):

    # Opening JSON file
    f = open(json_file, )

    # returns JSON object as a dictionary
    data = json.load(f)
    add_data = []
    # Iterating through the json
    # list
    body_key = None
    for i in data:
        if('body' in i and i['type'].lower() == "post"):
            # get body key
            for key in i['body'].keys():
                body_key = key

            if ('count' in i):
                count = int(i['count'])
            else:
                count = 1

            #generate post request based on count
            for y in range(0, count):
                #if more than one is generated
                dict_post = post_generate(i, body_key, id)
                add_data.append(dict_post)

                #if put option = 1, generate put cases for post req
                if (put_option == 1 and body_key in i['body']):
                    dict_put = put_generate(dict_post, body_key, id)
                    add_data.append(dict_put)

                #if option = 1, generate delete cases for post req
                if (del_option == 1 and id in i['body'][body_key]):
                    dict_delete = delete_generate(dict_post, body_key, id)
                    add_data.append(dict_delete)

        elif(i['type'].lower() == "delete"):
            add_data.append(i)

        elif ('body' in i and i['type'].lower() == "put"):
            # get body key
            for key in i['body'].keys():
                body_key = key

            # generate data for body content based on type given in JSON input
            for x in i['body'][body_key]:
                if (i['body'][body_key][x] == "int"):
                    i['body']['contact'][x] = fake.pyint()

                if (i['body'][body_key][x] == "string"):
                    i['body'][body_key][x] = fake.pystr()
            add_data.append(i)

    #write converted json into json
    DataFile = open("output.json", "w")
    DataFile.write(json.dumps(add_data, indent=4))
    DataFile.close()
    print("Generation Successful")

