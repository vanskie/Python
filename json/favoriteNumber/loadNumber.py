import json

filename = 'number.json'

with open(filename) as f_obj:
    username = json.load(f_obj)

print('Hello there {}!'.format(username))

