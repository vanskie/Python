class Restaurant():
    """Openes a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Prints the atributes"""

        print(self.restaurant_name)
        print(self.cuisine_type)


    def open_restaurant(self):
        """Opens the restaurant"""

        print('The restaurant is open for business!')


    def set_number_served(self, served):
        """Sets the number of served people"""
        self.number_served = served

    
    def increment_number_served(self, inc):
        """Increments the number of people served and checks
        to see if that number is less than before and if it 
        is doesent let the change happen
        """
        
        if inc < 0:
            print('Cannot increment by a negative number.')
        else:
            self.number_served += inc


class IceCreamStand(Restaurant):
    """Inherits from Restaurant and uses its atributes and methods
    to open an IceCreamStand"""

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    
    def set_flavors(self, *flavors):
        
        print('The flavors you chose are: ')

        for ice in flavors:
            print('\t- {}'.format(ice))
