import json

filename = 'number.json'
usernum = input('Enter your favorite number: ')

with open(filename, 'w') as f_obj:
    json.dump(usernum, f_obj)

