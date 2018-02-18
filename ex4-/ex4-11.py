pizza_list = ['Peperoni', 'Mediteriano', 'Italian', 'Margarita', 'American-Hot']
#Copying the list in another list and modifying them both seperately.
friends_list = pizza_list[:]

pizza_list.append('Banica')
friends_list.append('VitaBella')

print('My favorite pizzas are: \n')
for pizza in pizza_list:
	print(pizza)

print('My friends favorite pizzas are: \n')
for frizza in friends_list:
	print(frizza)