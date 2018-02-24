file_name = 'guest_list.txt'

guest = input('Could you please provide your name: ')

with open(file_name, 'w') as write_object:
    write_object.write(guest)

