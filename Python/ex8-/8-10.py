def print_name(names):
    """Print the names of the magicians"""

    for name in names:
        print(name)

def make_great(names):
    """Makes the all the magicians in the list 'great'!"""

    for index in range(0,len(names)):
        names[index] = names[index] + ' the Great!'

    return print_name(names)

magicians = []

while True:

    x = input('Enter magicians names, or enter q to exit and print the results\
    ')
    if x == 'q':
        break
    magicians.append(x)

make_great(magicians)

