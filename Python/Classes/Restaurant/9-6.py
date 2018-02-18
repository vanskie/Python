from restaurant import *

my_stand = IceCreamStand('Ice-ice', 'Baby')
my_stand.set_flavors('Vanilla', 'choco', 'pure-ice')

my_stand2 = IceCreamStand('nice-ice baby', 'ice-tea')
my_stand.set_flavors('nice-ice', 'cream puffs', 'other. idk')

my_stand.open_restaurant()

print(my_stand.number_served)
my_stand.increment_number_served(10)
print(my_stand.number_served)

