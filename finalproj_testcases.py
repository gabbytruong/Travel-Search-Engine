from finalproj import *
import unittest
import requests
import json

#need at least 15 tests

class TestNetState(unittest.TestCase):
    def test_netstate_data(self):
        t1 = get_netstate_data('mi')
        t2 = get_netstate_data('ca')
        t3 = get_netstate_data('md')

        self.assertEqual(t1,('Detroit', 'mi', '951,270'))
        self.assertEqual(t2,('Los Angeles', 'ca', '3,694,820'))
        self.assertNotEqual(t2, 'Los Angeles')
        self.assertEqual(len(t3), 3)
        self.assertEqual(t3, ('Baltimore', 'md','651,154'))

class TestYelpRestaurants(unittest.TestCase):
    def test_restaurant_data(self):

        t1 = get_restaurants('mi')
        t2 = get_restaurants('ca')
        t3 = get_restaurants('md')

        self.assertTrue('grey ghost detroit detroit' not in t1)
        self.assertTrue(('republic detroit 2',"['1942 Grand River Ave', 'Detroit, MI 48226']",
        '4.0', '391', '$$$') not in t1)
        self.assertTrue('4.0' not in t1)
        self.assertFalse('1443' in t2)
        self.assertFalse('2.0' in t3)


class TestYelpHotels(unittest.TestCase):
    def test_hotel_data(self):

        t1 = get_restaurants('mi')
        t2 = get_restaurants('ca')
        t3 = get_restaurants('md')

        self.assertTrue('$$$$' not in t1)
        self.assertFalse(('el moore detroit',
        "['624 W Alexandrine St', 'Detroit, MI 48201']",'5.0','13','$$$') in t1)
        self.assertTrue('60' not in t2)
        self.assertFalse('4.0' in t3)
        self.assertTrue('267' not in t3)



if __name__ == '__main__':
    unittest.main()
