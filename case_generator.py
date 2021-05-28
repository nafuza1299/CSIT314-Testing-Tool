import json
from faker import Faker

#input dictionary values for deletion
def delete_generate(dict_delete, i, body_key, id):
    dict_delete["url"] =  i['url'] + "/" + str(i['body'][body_key][id])
    dict_delete["check"]["url"] =  i['url'] + "/" + str(i['body'][body_key][id])
    dict_delete["header"] = i["header"]
    return dict_delete

#input dictionary values for updating
def put_generate(dict_put, i, body_key, id):
    dict_put["url"] = i['url'] + "/" + str(i['body'][body_key][id])
    dict_put["check"]["url"] = i['url'] + "/" + str(i['body'][body_key][id])
    for x in i['body'][body_key]:
        if (x != id):
            dict_put['body'][body_key][x] = i['body'][body_key][x]
    dict_put["header"] = i["header"]
    return dict_put


def run_generation(json_file, options = 0, id = None):
    fake = Faker()

    # Opening JSON file
    f = open(json_file, )

    # returns JSON object as a dictionary
    data = json.load(f)



    #template for deletion
    dict_delete =   {
        "url": None,
        "type":"DELETE",
        "header" :{
            None
        },
        "check":{
            "url": None,
            "success_code":"200"
        }
    }

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

    # Iterating through the json
    # list
    body_key = None
    for i in data:
        if('body' in i and i['type'].lower() == "post"):
            #get body key
            for key in i['body'].keys():
                dict_put['body'][key] = {}
                body_key = key

            #generate data for body content based on type given in JSON input
            for x in i['body'][body_key]:
                if(i['body'][body_key][x] == "int"):
                    i['body']['contact'][x] = fake.pyint()

                if(i['body'][body_key][x] == "string"):
                    i['body'][body_key][x] = fake.pystr()

            #if option = 1, generate delete cases for post req
            if (options == 1 and id in i['body'][body_key]):
                dict_delete = delete_generate(dict_delete, i, body_key, id)
                data.append(dict_delete)

            #if option = 2, generate put cases for post req
            if (options == 2 and body_key in i['body']):
                dict_put = put_generate(dict_put, i, body_key, id)
                data.append(dict_put)

        #if check key exists in JSON key, edit check url
        if 'check' in i:
            for x in i['check']:
                if 'url' in x and 'body' in i and id in i['body'][body_key]:
                    i['check'][x]= i['url'] + "/" + str(i['body'][body_key][id])

    #write converted json into json
    DataFile = open("output.json", "w")
    DataFile.write(json.dumps(data, indent=4))
    DataFile.close()
    print("Generation Successful")

