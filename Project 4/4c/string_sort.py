# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/18/2022
# Description: insertion sort function that accepts a list of strings as parameter and then sorts the string list in
# place - doesn't return anything; ignores case for input strings


def string_sort(str_list):
    """insertion sort that sorts list of strings in place ignoring case"""
    for index in range(1, len(str_list)):
        value = str_list[index].lower()  # lower case so that compared values ignore case
        pos = index - 1
        temp_str = str_list[index]  # added to set str_list[pos + 1] to this after while loop, since can't use value
        # as we need the mutated values to be the same case as the input values
        while pos >= 0 and value < str_list[pos].lower():  # again lower case to check placement in list ignoring case
            str_list[pos + 1] = str_list[pos]  # mutate pos + 1 if conditional passes
            pos -= 1
        str_list[pos + 1] = temp_str


# Tests
# string_list = ["maRker", "marble", "Zebra", "apple", "suvi", "SuVi"]
# print(string_list)
# string_sort(string_list)
# print(string_list)
