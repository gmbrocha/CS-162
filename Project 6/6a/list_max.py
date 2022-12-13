# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/31/2022
# Description: Recursive function that accepts a list of numbers as an argument, sets default arguments pos to zero and
# max_num to None; sets initial value for max_num; provides recursion break base case; checks current position in the
# list and whether that value is greater than the current max_num, sets max_num if so; performs recursion by passing the
# list, incremented position, and max_num back to itself


def list_max(num_list, pos=0, max_num=None):
    """recursive function that accepts a single user input list of numbers and returns the maximum value in that list"""
    if max_num is None:  # sets initial value of max_num
        max_num = num_list[pos]
    if pos == len(num_list) - 1:  # base case that returns current max_num when pos == index at end of list
        return max_num
    if num_list[pos] > max_num:  # conditional that checks recursive pos (pos + 1) against current max_num, sets max if
        max_num = num_list[pos]
    return list_max(num_list, pos + 1, max_num)  # recursion to pass num_list, next position, and current max_num back
    # to list_max
