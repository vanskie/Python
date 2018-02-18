from restaurant import *

pizza = Restaurant('Pizzaria', 'pizza')

pizza.describe_restaurant()
pizza.open_restaurant()
print('The restaurant is a {}.'.format(pizza.restaurant_name))

