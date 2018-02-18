def name_print(names):
    """Prints the given names"""

    for name in names:
        print(name)

magicians = []
flag = True

while flag:
    if flag == False:
        break

    x = input('Enter magicians names, or enter q to print the names and exit\
    the program: ')
    magicians.append(x)

    if x == 'q':
        flag = False

name_print(magicians)

