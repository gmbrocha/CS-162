# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/18/2022
# Description: Defines 2 functions - a bubble sort and an insertion sort and adjusts counters for number of comparisons
# and exchanges made during sorting of input lists; both return tuples containing comparison # and exchange #


def bubble_count(user_list):
    """sorts an input list in ascending order by bubble sort algorithm and counts comparisons and exchanges"""
    comp = 0  # counter for comparisons
    exch = 0  # counter for exchanges
    for n in range(len(user_list) - 1):
        for index in range(len(user_list) - 1 - n):
            comp += 1
            if user_list[index] > user_list[index + 1]:
                exch += 1
                temp = user_list[index]  # hold value at index because next line will mutate the value in the list
                user_list[index] = user_list[index + 1]  # mutate value at index to be the value to the immediate right
                user_list[index + 1] = temp  # use temp value from above to set index + 1 to original index value
    return comp, exch


def insertion_count(user_list):
    """sorts an input list in ascending order by insertion sort algorithm and counts comparisons and exchanges"""
    comp = 0  # counter for comparisons
    exch = 0  # counter for exchanges
    for index in range(1, len(user_list)):
        value = user_list[index]
        pos = index - 1
        while pos >= 0:  # remove the second part of boolean from template; explained in line 32 comment
            comp += 1
            if value < user_list[pos]:  # separated this conditional from the while loop in the original so
                # that comp would increment for every comparison of value and user_list[pos] and not just the times when
                # while A and B would be True
                user_list[pos + 1] = user_list[pos]
                exch += 1  # increment exchange
                pos -= 1  # decrement position to check value against next value to left until pos < 0; primary
                # condition for termination
            else:  # break loop if value >= user_list[pos]; auxiliary condition for termination
                break
        user_list[pos + 1] = value  # sets leftmost value after the while loop to current 'pulled' value; if inner
        # conditional is False, pos will simply be equal to index and nothing will change
    return comp, exch

