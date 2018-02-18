def build_profile(fname, lname, **user_info):
    """Builds a user profile with the given arguments."""
    body = ''
    header = fname.title() + ' ' + lname.title() + ':\n'\
    + 'aditional info: \n'

    for key, value in user_info.items():
        body += key + ' <> ' + str(value) + '\n'
    
    result = header + body

    return print_profile(result)

def print_profile(x):
    return print(x)

build_profile('Ivan', 'Vasilev', city = 'Burgas', age = 23, sex = 'male')

