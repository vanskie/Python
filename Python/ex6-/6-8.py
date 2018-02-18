pet_0 = {
    'type': 'Iguana',
    'Owner': 'Matthew',
    'food': 'Insects',
    'name': 'D-rex',
    }

pet_1 = {
    'type': 'Lion',
    'Owner': 'Jimmy',
    'food': 'Other animals',
    'name': 'Mufasa',
    }

pet_2 = {
    'type': 'fish',
    'Owner': 'Ellen',
    'food': 'fish-food',
    'name': 'Dorothy(Dory)',
    }

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print('The {}\'s name is {}, {} is the owner. {} eats {} by the way'\
    .format(pet['type'], pet['name'], pet['Owner'], pet['name'],\
    pet['food'].lower()))

