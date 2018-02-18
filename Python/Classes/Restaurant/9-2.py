from restaurant import *

restaurants = {}

while True:

    rest_name = input(
    'Enter the name of the restaurant or '+
    'enter q to quit: ')
    rest_cuis = input('Enter cuisine or q to quit: ')

    if rest_name == 'q' or rest_cuis == 'q':
        break

    restaurants[rest_name] = rest_cuis

for key, value in restaurants.items():
    current = Restaurant(key, value)
    current.describe_restaurant()

