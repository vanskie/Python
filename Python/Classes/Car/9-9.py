from car import *

my_car = Car('honda', 'civic', '2015', 'white')
tesla = ElectricCar('tesla', 'model s', '2016', 'cherry red')

my_car.show_info()
print('My car still has no characteristics.\
we should call set_info()')
my_car.set_info()

my_car.show_info()

print('Now lets see the tesla')
tesla.show_info()
tesla.set_info()
tesla.show_info()

tesla.battery.get_range()
tesla.battery.upgrade_battery(100)
tesla.battery.get_range()




