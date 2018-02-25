import json

filename = 'user.json'

def login_check():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def new_user():
    username = input('Enter your username here it will be remembered: ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

def greet_user():
    if login_check():
        print('Hello there {}'.format(login_check()))
    else:
        new_user()
        
def check_user():
    if login_check():
        print('Is this your username - {}'.format(login_check()))
        choice = input('y/n: ')
        if choice == 'y':
            greet_user()
        elif choice == 'n':
            new_user()
    else:
        new_user()


check_user()

