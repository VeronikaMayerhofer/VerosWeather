import json

def read_config():
    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
        print("Read successful")
    print(data)
    a = '\u00b0'
    print(a)

read_config()