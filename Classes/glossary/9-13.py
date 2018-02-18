from collections import OrderedDict

glossary = OrderedDict()

while True:
    
    name = input('Enter your name: ')
    language = input('Enter your favorite language: ')
    if name == 'q' or language == 'q':
        break
    else:
        glossary[name] = language

for key, value in glossary.items():
    print('{}\'s favorite language is {}.'.format(key, value))


