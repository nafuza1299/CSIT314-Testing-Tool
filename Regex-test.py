import json
from faker import Faker
fake = Faker()

# Opening JSON file
f = open('data.json', )

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    if 'body' in i:
        #generate data for body content based on type given in JSON input
        for x in i['body']['contact']:
            if(i['body']['contact'][x] == "int"):
                i['body']['contact'][x] = fake.pyint()

            if(i['body']['contact'][x] == "string"):
                i['body']['contact'][x] = fake.pystr()

            print(x, i['body']['contact'][x])

    #if check key exists in JSON key, edit check url
    if 'check' in i:
        for x in i['check']:
            if 'url' in x and 'body' in i and 'id' in i['body']['contact']:
                print(x)
                i['check'][x]= i['url'] + "/" + str(i['body']['contact']['id'])


#write converted json into json
DataFile = open("output.json", "w")
DataFile.write(json.dumps(data, indent=4))
DataFile.close()

