import json

filename = 'number.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input('Enter your favorite number, we\'ll remember it for\
next time: ')
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print('Eyyyyyy ma man, wasn\'t your favorite number {} ;)'.format(
    number))

