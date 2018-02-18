person_0 = {
    'first_name': 'Ivan',
    'last_name': 'Vasilev',
    'age': 23,
    'city': 'Burgas',
    }

person_1 = {
    'first_name': 'Zornitsa',
    'last_name': 'Vasileva',
    'age': 21,
    'city': 'Burgas',
    }

person_2 = {
    'first_name': 'Stefan',
    'last_name': 'Vichev',
    'age': 23,
    'city': 'Burgas',
    }

person_3 = {
    'first_name': 'Valentina',
    'last_name': 'Vasileva',
    'age': 54,
    'city': 'Sarafovo'
    }

people = [person_0, person_1, person_2, person_3]

for person in people:
    print('Hello {} {} from {} age {}. How are you today?'.format(\
    person['first_name'], person['last_name'], person['city'],\
    person['age']))

     
