file_name = 'learning_python.txt'

with open(file_name) as all_file:
    all_at_once = all_file.read()

print('Now printing the contents all at once with the read() method\n')
print(all_at_once.rstrip())

print('\nNow printing the contents one line at a time\n')

with open(file_name) as line_file:
    for line in line_file:
        print(line.rstrip())

print('\nNow storing each line in a list with the readline() method,\
and working with the info from the file even after we close it.\n')

with open(file_name) as list_file:
    text = list_file.readlines()

print('\nNow printing the list:')
print(text)

