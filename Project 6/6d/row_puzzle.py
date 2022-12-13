# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/2/2022
# Description: function that accepts a list of numbers and completes a 'game' where the list indices are 'squares' and
# a token is placed on each square; the value at that index allows for the token to be moved left or right; if movement
# causes the token to be placed out of the range of the squares or a square that has already had the token placed on it,
# the function will try the alternate movement; if both tries fail, the game is unsolvable and the function returns
# false; it will try routes continuously until failing or 'winning' by placing the token on the last square which will
# always be 0 value


def row_puzzle(row_list, pos=0, temp_list=None):
    """function to iterate through list by jumping indices according to value at current index; provides base cases
    for completion of the iteration 'game', out of range indices, and already used indices; tries both right and left
    choices for each index pos utilized"""
    if temp_list is None:  # initialize temporary list with comprehension to preserve row_list
        temp_list = [n for n in row_list]
    if pos < 0 or pos >= len(row_list):  # covers out of range base case
        return False
    if temp_list[pos] == ".":  # base case for a repeat square
        return False
    if pos == len(row_list) - 1:  # base case for successfully reaching end of row
        return True
    temp_list[pos] = "."
    try_route = row_puzzle(row_list, pos + row_list[pos], temp_list)  # try going right
    if try_route is False:  # if used index or out of range check the left choice
        try_route = row_puzzle(row_list, pos - row_list[pos], temp_list)  # try going left
        if try_route is False:  # if used index or out of range return False; neither right nor left works
            return False
        elif try_route is True:  # if pos is the end of the row return true and back out of recursion
            return True
    elif try_route is True:  # provides last case where going right each choice works to solve
        return True






