from finalproj import *
import unittest
import requests
import json

#need at least 15 tests

class TestNetState(unittest.TestCase):
    def test_netstate_data(self):
        t1 = finalproj.get_netstate_data('mi')
        t2 = finalproj.get_netstate_data('ca')
        t3 = finalproj.get_netstate_data('md')

        self.assertEqual(t1,'Detroit, MI: population of 951,270')
        self.assertEqual(t2,'Los Angeles, CA: population of 3,694,820')
        self.assertNotEqual(t2, 'Los Angeles')
        self.assertNotEqual(t3, '651,154')
        self.assertEqual(t3, 'Baltimore, MD: population of 651,154')


class TestYelpRestaurants(unittest.TestCase):
    def test_restaurant_data(self):

        t1 = finalproj.get_restaurants('mi')
        t2 = finalproj.get_restaurants('ca')
        t3 = finalproj.get_restaurants('md')

        self.assertTrue('GREY GHOST DETROIT DETROIT' in t1)
        self.assertTrue('LADY OF THE HOUSE DETROIT' in t1)
        self.assertTrue("['One Park Ave', 'Detroit, MI 48226']" in t1)
        self.assertFalse('Number of reviews: 1443' not in t2)
        self.assertFalse('Rating: 2.0' not in t3)


class TestYelpHotels(unittest.TestCase):
    def test_hotel_data(self):

        t1 = finalproj.get_restaurants('mi')
        t2 = finalproj.get_restaurants('ca')
        t3 = finalproj.get_restaurants('md')

        self.assertFalse('Price range: $$$$$' not in t1)
        self.assertTrue('Price range: $$' in t2)
        self.assertTrue('FREEHAND LOS ANGELES LOS ANGELES' in t2)
        self.assertFalse('BIDDLE STREET INN BALTIMORE' not in t3)
        self.assertTrue('THE IVY HOTEL BALTIMORE' in t3)



if __name__ == '__main__':
    unittest.main()
