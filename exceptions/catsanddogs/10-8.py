dog_file = 'dogs.txt'
cat_file = 'cats.txt'

try:
    with open(dog_file) as dog_object:
        for name in dog_object:
            print('This dogs name is {}!'.format(name.rstrip()).rstrip())
except FileNotFoundError:
    #print('The file doesen\'t seem to be present in this directory!')
    #lets make this exception fail silently.
    pass
try:
    with open(cat_file) as cat_object:
        for name in cat_object:
            print('This cats name is {}!'.format(name.rstrip()).rstrip())
except FileNotFoundError:
    pass

