# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/01/2022
# Description: function that accepts two argument strings and determines whether one of the strings is a subsequence of
# the other; provides two base cases to exit recursion; advances string indices based on condition of compared chars in
# the strings


def is_subsequence(str_a, str_b, ind1=0, ind2=0):
    """function to determine whether str_a is a subsequence of str_b or not, returns True or False based on this
    condition"""
    if ind1 == len(str_a):  # a 'race' to see which finishes first - base case 1 and 2 terminate with return value if
        # one string finishes before the other - if str_a finishes first, the 'subsequent' string is valid
        return True
    if ind2 == len(str_b):  # if str_b finishes first, then the chars of str_a haven't been accounted for and is not sub
        return False
    if str_a[ind1] == str_b[ind2]:  # if the chars are the same, advance both indexes for both strings for recursion
        return is_subsequence(str_a, str_b, ind1 + 1, ind2 + 1)
    else:  # if the chars are not the same, only advance str_b index for the recursion
        return is_subsequence(str_a, str_b, ind1, ind2 + 1)
