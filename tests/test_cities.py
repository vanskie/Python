from city_functions import city_country
import unittest

class TestCity(unittest.TestCase):
    """Tests the output of city_functions"""

    def test_city_country(self):
        test0 = city_country('santiago', 'chile')
        self.assertEqual(test0, 'santiago, chile')

unittest.main()

