places = {
    'Ivan': ['Burgas', 'Kameno', 'Duesseldorf'],
    'Zori': ['Burgas', 'Home with me'],
    }

for names in places:
    print(names + ':')
    for place in places[names]:
        print('\n\t' + place)

