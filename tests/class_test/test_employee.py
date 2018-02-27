from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """Testing the employee class"""

    def setUp(self):
        fname = 'Shaquan'
        lname = 'Shaquin'
        salary = 30000
        self.employee0 = Employee(fname, lname, salary)

    def test_default_raise(self):
        method = self.employee0.give_default_raise()
        self.assertEqual(method, 35000)

    def test_custom_raise(self):
        method = self.employee0.give_default_raise(1000)
        self.assertEqual(method, 31000)

unittest.main()

