# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/17/2022
# Description: Modification of binary search function to return a user defined exception if the search target not found
# in the list


class TargetNotFound(Exception):
    """User defined exception for target not found in binary search"""
    pass


def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of the target parameter, if not found raises the TargetNotFound exception and
    notifies the user that the target isn't within the list
    """
    try:
        first = 0
        last = len(a_list) - 1
        while first <= last:
            middle = (first + last) // 2  # divide list into half lists by floor
            if a_list[middle] == target:  # if middle index is the target; stop and return that value
                return middle
            if a_list[middle] > target:  # if middle index value is greater than target; make last value the middle - 1
                # which notifies loop that the target is in the first half of the list - the decrement will shorten this
                # first half list until loop terminates at middle == target which returns middle - if not, except
                last = middle - 1
            else:  # if middle index value is less than target; make first value the middle + 1 which notifies loop that
                # the target is in the second half of the list - this increment will make the 'second half' of list
                # shorter for each iteration until loop terminates at middle == target which returns middle - if not,
                # except
                first = middle + 1
        raise TargetNotFound  # if middle never gets returned, will raise TargetNotFound
    except TargetNotFound:  # calls TargetNotFound for the raised exception
        print("Search target not found.")


