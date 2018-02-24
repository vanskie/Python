while True:
    number0 = input('Enter first number to be summed or q: ')
    if number0 == 'q':
        break
    number1 = input('Enter a second number or q: ')
    if number1 == 'q':
        break

    try:
        print(int(number0) + int(number1))
    except ValueError:
        print('Please provide only integers!')


