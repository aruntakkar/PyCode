import json
from pprint import pprint

data = open('petsjson.txt', 'rb').read().decode()
pets = json.loads(data)

pprint(pets)
