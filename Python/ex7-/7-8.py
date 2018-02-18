sandwich_orders = ['Mcrib', 'Tuna', 'Toast']
finished_sandwiches = []

while sandwich_orders:

    current = sandwich_orders.pop()
    print('Making your {} sandwich.'.format(current))
    finished_sandwiches.append(current)

for sandwich in finished_sandwiches:
    print('Your {} sandwich is ready.'.format(sandwich))


print('Len of sandwich_orders is {}.'.format(len(sandwich_orders)))
print('\nLen of finished_sandwiches is {}.'.format(len(finished_sandwiches))) 

