class Car():
    """This is a class representation of a car"""

    def __init__(self, maker, model, year, color):
        
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.info = []

    def set_info(self):
        """Puts all the car info into a list"""

        self.info.append(self.maker)
        self.info.append(self.model)
        self.info.append(self.year)
        self.info.append(self.color)

    def show_info(self):
        """Prints the car info in a neat format!"""

        print('Car characteristics:\n')
        for item in self.info:
            print(item)


class Battery():
    """This is a model of a battery"""

    def __init__(self):
        self.capacity = 49 


    def get_range(self):
        """Outputs the range of the vehicle and battery"""
        
        if self.capacity > 50:
            print('The battery range for this vehicle is > 50')
        else:
            print('The battery range for this vehicle is < 50')
   
    
    def upgrade_battery(self, upgrade):
        """Upgrades the battery and overall range"""
        
        self.capacity += upgrade


class ElectricCar(Car):
    """This is a child class representation of an electric car"""

    def __init__(self, maker, model, year, color):
        super().__init__(maker, model, year, color)
        self.battery = Battery()


