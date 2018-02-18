sandwich_orders = ['Mcrib', 'pastrami', 'pastrami', 'Tuna', 'pastrami',\
'Toast', 'pastrami']
finished_sandwiches = []

print('FYI to all customers, we\'ve ran out of pastrami')
out_of = 'pastrami'

while out_of in sandwich_orders:
    sandwich_orders.remove(out_of)

while sandwich_orders:

    current = sandwich_orders.pop()
    print('Making your {} sandwich.'.format(current))
    finished_sandwiches.append(current)

for sandwich in finished_sandwiches:
    print('Your {} sandwich is ready.'.format(sandwich))


print('Len of sandwich_orders is {}.'.format(len(sandwich_orders)))
print('\nLen of finished_sandwiches is {}.'.format(len(finished_sandwiches))) 

