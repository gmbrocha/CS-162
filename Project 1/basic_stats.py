# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 9/22/2022
# Description: Short script that imports functions from the statistics module; uses class Student to initialize objects
# with name and grade data members; uses a short function that accepts a list of Student objects and performs basic
# statistics on the grade elements of those objects

from statistics import mean, median, mode


class Student:
    """initializes student objects with name and grade"""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade


def basic_stats(stud_list):
    """calls statistics functions on the grade data members from student objects"""
    temp_list = []
    for item in stud_list:
        temp_list.append(item.get_grade())
    stat_tuple = (mean(temp_list), median(temp_list), mode(temp_list))
    return stat_tuple
