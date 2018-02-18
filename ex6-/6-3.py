glossary = {}

glossary['and'] = 'A python evaluation keyword where a and b must both \
be True or False for the evaluation to be True\n'
glossary['or'] = 'A python evaluation keyword where a or b must be \
True for the evaluation to be true. If both of them are False the \
evaluation is also false\n'
glossary['for'] = 'A python keyword signifying a loop, a for loop to be exact.\
\nA for loop is a loop in which we can set a range() function or \
loop through a set of items like in a list or a dicitionary etc.\n'

for word in glossary:
    print('{}:\n{}'.format(word, glossary[word]))

