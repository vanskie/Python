books = ['moby_dick.txt', 'huckleberry_fin.txt']

for book in books:
    with open(book) as book_obj:
        big_line = book_obj.read()
        print('The word \'the\' appears in {} {} times'.format(
        book, str(big_line.lower().count('the'))))

