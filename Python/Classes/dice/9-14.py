from dice import Die

while True:
    current = Die()

    die = input('What kind of die do you want: ')
    if die == 'q':
        break
    times = input('How many times do you want to roll the die: ')
    if times == 'q':
        break

    if die == '':
        current.roll_dice(int(times))
    else:
        current.sides = int(die)
        current.roll_dice(int(times))

