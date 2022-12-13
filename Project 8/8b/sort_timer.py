# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/14/2022
# Description: program provides two decorated functions, bubble and insertion sort, that have the added capability of
# sort_timer added which contains a wrapper function to calculate the execution time of the wrapped function via the
# time module. The function compare sorts creates random (0-10000) integer lists (1000-10000; 1000 element increments)
# that are passed to the decorated sort functions. The return values (sort execution in seconds) are then appended to
# two lists (bubble_y and insertion_y) that are used by pyplot as y-values for line graph display. The graph displayed
# contains time (s) as its y-axis and number of elements sorted as its x-axis.

import random
import time
from functools import wraps
from matplotlib import pyplot


def sort_timer(func):
    """decorator function to return the duration of execution of a passed function; uses time module method to calculate
    the beginning and end times, and then return the difference"""
    @wraps(func)  # wraps decorator to provide the name and docstring of the decorated function being passed
    def wrapper(a_list):
        begin = time.perf_counter()  # use time method perf_counter to store begin time
        func(a_list)  # call decorated function and pass list
        end = time.perf_counter()  # store end time
        dur = end - begin  # calculate time difference and return
        return dur
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order by bubble method, decorated with sort_timer function"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order by insertion method, decorated with sort_timer function"""
    for index in range(1, len(a_list)):  # index = ECX
        value = a_list[index]  # value = [EBX]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(func1, func2):
    """takes two sort functions and compares the time it takes to sort varying lengths of lists of random integers (from
    1-10000) with 1000 to 10000 elements per list (increments of 1000); uses decorated versions of bubble sort and
    insertion sort that return the difference in seconds from begin to end of sort; stores those values in appropriate
    lists that will become y-value inputs for the pyplot call and display; will display line graphs of each sort method
    time complexity increase over time"""
    bubble_y = []  # will hold y-values for bubble sort (these values are in seconds)
    insertion_y = []  # will hold y-values for insertion sort (these values are in seconds)
    upper = 1000  # set random list number of elements
    for i in range(0, 10):  # increase the upper by 1000, ten times
        rand_list = []  # reset random list
        for n in range(0, upper + 1):
            rand = random.randint(1, 10000)  # generate random int and append to random list
            rand_list.append(rand)
        upper += 1000  # increase upper by 1000 for next list
        rand_list_copy = list(rand_list)  # create a copy of random list for use by second function
        t1 = func1(rand_list)  # call decorated bubble sort function
        t2 = func2(rand_list_copy)  # call decorated insertion sort function
        bubble_y.append(t1)
        insertion_y.append(t2)  # append both time differences to their respective y-value lists for use in display
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], bubble_y, 'ro--', linewidth=2, label='bubble sort')
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], insertion_y, 'go--', linewidth=2, label='insertion sort')
    pyplot.xlabel("n * 1000 elements")  # I kept this as n * 1000 and the small n's for the x-axis for aesthetic, not
    # sure if allowed, but it looks much nicer than 1000, 2000, etc. which wouldn't fit well on the axis
    pyplot.ylabel("time (s)")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)  # call the main function and pass the decorated goodies to it
