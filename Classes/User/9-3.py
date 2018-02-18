from user import *

user_info = {}

while True:

    first_name = input('Enter your first name or q to quit: ')
    if first_name == 'q':
        break
    
    last_name = input('Enter your last name or q: ')
    if last_name == 'q':
        break

    password = input('Enter your password or q: ')
    if password == 'q':
        break

    user_info[first_name[0] + last_name[0]] = first_name, last_name, password


for key, value in user_info.items():
    
    User(value[0], value[1], value[2]).greet_user()

test = User('testname', 'testlastname', 'test')

test.describe_user()

