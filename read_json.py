import json

f = open('words.json', "r")

data = json.loads(f.read())


def read_data(x=None):
    return data if x == None else data[x]


f.close()
