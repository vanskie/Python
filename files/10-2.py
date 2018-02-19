file_name = 'learning_python.txt'

with open(file_name) as before_change:
    for line in before_change:
        print(line.rstrip())

print('\nNow lets change every \'python\' into \'C\'.\n')

with open(file_name) as change_line:
    for line in change_line:
        print(line.replace('Python', 'C').rstrip())
        

