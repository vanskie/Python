poll = {}

while True:

    name = input('Could you gives us your name before we begin: ')

    if name == 'quit':
        break

    response = input('If you could go anywhere in this world,\
    where would you go?\n')
    
    
    print('\n\tIf you want to stop giving input type exit or quit')

    poll[name] = response

for key, value in poll.items():
    print('{} would love to visit: {}.'.format(key, value))
    
