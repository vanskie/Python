file_name = 'guest_book.txt'

while True:
    name = input('Enter your name here or q to quit: ')
    if name == 'q':
        break
    print('Hello {} we are honored you\'re our guest.'.format(name))

    with open(file_name, 'a') as guest_book:
        guest_book.write(name + '\n')


