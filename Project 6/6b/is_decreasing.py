# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/1/2022
# Description: Function that accepts a list of numbers as the sole argument, sets default value for position,
# and performs recursion through the list checking if all the values in the list are in strictly decreasing
# order; returns True is decreasing, False if otherwise


def is_decreasing(num_list, pos=0):
    """function accepts list of numbers and returns True if the list is strictly decreasing; otherwise returns False"""
    value = num_list[pos]  # set value to be compared
    if pos == len(num_list) - 1:  # base case 1, if the recursion completes  without returning will return true
        return True
    if num_list[pos + 1] >= value:  # base case 2, if the condition passes will return false
        return False
    return is_decreasing(num_list, pos + 1)  # call to function for recursion
