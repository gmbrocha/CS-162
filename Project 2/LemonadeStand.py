# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/5/2022
# Description: script that creates objects within three classes (menuItems, salesForDay, lemonadeStand) and uses
# references to each to determine sale volume, profit per item, profit per day, and total profit for lemonadeStand
# objects

class InvalidSalesItemError(Exception):
    """user defined exception for handling invalid items passed in a dictionary to a method"""
    pass


class MenuItem:
    """creates MenuItem objects with data members name, wholesale cost, and sell price; provides get methods for these
    data members"""

    def __init__(self, name, whole_cost, sell_price):
        """initializes MenuItem objects"""
        self._name = name
        self._whole_cost = whole_cost
        self._sell_price = sell_price

    def get_name(self):
        """get method for name"""
        return self._name

    def get_whole_cost(self):
        """get method for wholesale cost"""
        return self._whole_cost

    def get_sell_price(self):
        """get method for sale price"""
        return self._sell_price


class SalesForDay:
    """creates objects SalesForDay with data members for which day and a dictionary containing MenuItem objects with
    names as keys"""

    def __init__(self, open_days, sales_dict):
        """initializes SalesForDay objects"""
        self._open_days = open_days
        self._sales_dict = sales_dict

    def get_day(self):
        """get method for day of sale"""
        return self._open_days

    def get_sales_dict(self):
        """get method for dict containing MenuItem objects"""
        return self._sales_dict


class LemonadeStand:
    """creates LemonadeStand objects with a name parameter; day, menu dict and sales list all initialized empty or 0"""

    def __init__(self, name):
        """Initializes LemonadeStand objects"""
        self._name = name
        self._day = 0
        self._menu_dict = {}
        self._sales_list = []

    def get_name(self):
        """get method for stand name"""
        return self._name

    def add_menu_item(self, item):
        """method that adds MenuItem objects for the menu dict with names of items as keys and objects as values"""
        self._menu_dict[item.get_name()] = item

    def enter_sales_for_today(self, today_sales):
        """method to enter a dict of todays sales; handles exceptions for invalid MenuItem names"""
        try:
            for key in today_sales:
                if key not in self._menu_dict:
                    raise InvalidSalesItemError
            self._sales_list.append(SalesForDay(self._day, today_sales))
            self._day += 1
        except InvalidSalesItemError:
            print("There is an invalid item in the sale dictionary.")

    def sales_of_menu_item_for_day(self, day, name):
        """method to total the sale of any one item per day passed as parameter"""
        if name in self._sales_list[day].get_sales_dict():
            return self._sales_list[day].get_sales_dict()[name]
        else:
            return 0

    def total_sales_for_menu_item(self, item_name):
        """method to total sales of any one item for all days"""
        total_sold = 0
        for n in range(0, self._day):
            total_sold += self.sales_of_menu_item_for_day(n, item_name)
        return total_sold

    def total_profit_for_menu_item(self, item_name):
        """method to calculate profit per item and multiply that by total sales"""
        return (self._menu_dict[item_name].get_sell_price() - self._menu_dict[item_name].get_whole_cost()) * \
               self.total_sales_for_menu_item(item_name)

    def total_profit_for_stand(self):
        """method that calculates profit of all items over all days for a LemonadeStand object"""
        total_profit = 0
        for element in self._menu_dict:
            total_profit += self.total_profit_for_menu_item(element)
        return total_profit


def main():
    """function defining main execution"""
    stand_one = LemonadeStand('Lemonade Is Good')
    item_1 = MenuItem('lemonade', 0.25, 1.75)
    stand_one.add_menu_item(item_1)
    item_2 = MenuItem('hamsters', 0.6, 2.5)
    stand_one.add_menu_item(item_2)

    day_0_sales = {
        'lemonade': 4,
        'hamsters': 10
    }
    day_1_sales = {
        'lemonade': 15,
        'hamsters': 0,
        'lobsters': 1
    }

    stand_one.enter_sales_for_today(day_0_sales)
    stand_one.enter_sales_for_today(day_1_sales)


if __name__ == '__main__':
    main()

# print(stand.sales_of_menu_item_for_day(1, "lemonade"))
# print(stand.sales_of_menu_item_for_day(1, "cookie"))
# print(stand.sales_of_menu_item_for_day(0, "nori"))
# print("cookie total sales = ", stand.total_sales_for_menu_item('cookie'))  # print the total sales for cookie
# print("cookie total profit = ", stand.total_profit_for_menu_item('cookie'))
# print("Stand total profit = ", stand.total_profit_for_stand())  # print the total profit for stand
