from restaurant import *

restaurant = Restaurant('Pizzeria', 'Pizza')
print(restaurant.number_served)
restaurant.number_served = 15
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(-1)
restaurant.increment_number_served(100)
print(restaurant.number_served)

