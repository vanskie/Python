def print_names(names):
    """Prints the list of names provided."""

    for name in names:
        print(name)

def make_great(copy_names):
    """Makes every magician great but from a copied list not the original"""

    for index in range(0,len(copy_names)):
        copy_names[index] = copy_names[index] + ' the Great!'

    return print_names(copy_names)

magicians = []

while True:

    x = input('Enter magician name, or q if you want to end the program: ')
    if x == 'q':
        break
    magicians.append(x)

print_names(magicians)
make_great(magicians[:])
print_names(magicians)


