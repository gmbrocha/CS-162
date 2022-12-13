# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/5/2022
# Description: script to unit test the LemonadeStand.py code

import unittest
from LemonadeStand import LemonadeStand, MenuItem, SalesForDay


class TestMenuItem(unittest.TestCase):
    """contains unit tests for the class MenuItem"""

    def test_0(self):
        """test init and get methods"""
        item_1 = MenuItem("chicken", 1.0, 3.5)
        self.assertEqual(item_1.get_name(), "chicken")
        self.assertEqual(item_1.get_whole_cost(), 1.0)
        self.assertEqual(item_1.get_sell_price(), 3.5)


class TestSalesForDay(unittest.TestCase):
    """contains unit tests for the class SalesForDay"""

    def test_1(self):
        """test init and get methods"""
        dict_1 = {
            "lemons": 1
        }
        sale_day_1 = SalesForDay(2, dict_1)
        self.assertEqual(sale_day_1.get_day(), 2)
        self.assertEqual(sale_day_1.get_sales_dict(), dict_1)


class TestLemonadeStand(unittest.TestCase):
    """contains unit tests for the class LemonadeStand"""

    def test_2(self):
        """test init and get name methods"""
        stand_1 = LemonadeStand("fabricio's famous lemonade")
        self.assertEqual(stand_1.get_name(), "fabricio's famous lemonade")

    def test_3(self):
        """test add menu item method"""
        item_2 = MenuItem("hamsters", 0.5, 1.0)
        stand_2 = LemonadeStand("hamsters are delicious")
        dict_2 = {
            "hamsters": item_2
        }
        stand_2.add_menu_item(item_2)
        self.assertEqual(stand_2._menu_dict, dict_2)

    def test_4(self):
        """test enter_sales_for_today method"""  # the user defined exception still in original code will throw
        # can't get this to do anything, I'm a bit lost
        item_3 = MenuItem("gourds", 0.24, 0.34)
        today_sales = {
            "gourds": 4
        }
        stand_3 = LemonadeStand("lemons and gourds")
        stand_3.enter_sales_for_today(today_sales)
        self.assertEqual(stand_3._day, 0)
        self.assertEqual(stand_3._sales_list[0].get_sales_dict(), today_sales)


if __name__ == '__main__':
    unittest.main()
