# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/14/2022
# Description: a generator function that yields spoken-to-number strings so that each subsequent yield has values that
# are a number of and the actual number of the previous value. The generator function is count_seq which utilizes
# next_string() to parse the input string for numbers of numbers and then concatenates those to return a new string

def next_string(y_str):
    """helper function for count seq generator that will return a spoken-to-number version of an input string"""
    temp_str = ""
    num_count = 1
    index = 1  # will be used to break loop once we have iterated over every number in the input string
    for n in range(0, len(y_str)):  # this could be any number greater than the length of the string
        y_str += "-"  # added so that there is no range error on the conditional in the next loop
        for val in range(n, len(y_str) - 1):
            if y_str[val + 1] != y_str[val]:  # if the subsequent term is different, edit the temp str to reflect
                # numbers already iterated through
                temp_str += str(num_count) + str(y_str[val])  # add number count + current value in string to temp str
                num_count = 1  # reset number count to 1
                index += 1
            else:
                num_count += 1
                index += 1
        y_str = y_str[:-1]  # remove extra character added above
        if index > len(y_str):
            break
    return temp_str


def count_seq():
    """generator function that yields the strings created with the helper function above"""
    yield "2"  # handles first yield
    new_string = "12"  # will get yielded second
    while True:
        yield new_string
        new_string = next_string(new_string)  # assign the helper function return to variable to yield in iteration
