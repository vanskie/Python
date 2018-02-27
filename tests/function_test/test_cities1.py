from city_functions import city_country
import unittest

class TestCity(unittest.TestCase):
    def test_city_country(self):
        testcase = city_country('Sofia', 'Bulgaria')
        self.assertEqual(testcase, 'Sofia, Bulgaria')

unittest.main()

