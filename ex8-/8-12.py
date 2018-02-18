def sandwich_make(*ingredients):
    """Makes and prints a summary of the sandwich"""

    print('Here we have a sandwich with:\n')
    for item in ingredients:
        print('\t- ' + item)


sandwich_make('salami', 'tomatoes', 'chees')
sandwich_make('tomatoes', 'chees', 'ketchup', 'extra bread')
sandwich_make('3 olives', 'parmezhan')
        
