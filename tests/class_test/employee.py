class Employee():
    """
    A simple class to represent an employee.
    """
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_default_raise(self, bonus=5000):
        self.salary += bonus
        return self.salary

