# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/23/2022
# Description: A class example that defines creation of NobelData objects; provides init method to instantiate with
# json dictionary; provides method for searching json dictionary for the surnames of Nobel Prize winners for a chosen
# date and category

import json


class NobelData:
    """defines creation of NobelData objects; provides init method to instantiate with json dictionary; provides method
    for searching json dictionary for the surnames of Nobel Prize winners for a chosen date and category"""

    def __init__(self):
        """instantiate object and create empty private dict; use json load method to populate the private dict from
        external json file"""
        self._dict = {}  # create empty dictionary to hold json data
        with open("nobels.json", "r") as infile:
            self._dict = json.load(infile)  # load infile into the dictionary

    def search_nobel(self, year, category):
        """search method that accepts as parameters year and category and assigns them to self; the method then iterates
        through the json dict to find the surnames of the winners from that year and category; returns a sorted list
        of those surnames"""
        temp_list = []  # create list to hold surnames

        for n in range(0, len(self._dict["prizes"])):  # iterate through the prize key of the json dict
            if self._dict["prizes"][n]["year"] == year and self._dict["prizes"][n]["category"] == category:
                # conditional above to check for year and category parameters to begin inner loop
                for index in range(0, len(self._dict["prizes"][n]["laureates"])):  # iterate through laureate sublist
                    temp_list.append(self._dict["prizes"][n]["laureates"][index]["surname"])  # append surname from sub

        for n in range(1, len(temp_list)):  # insertion sort to alphabetize the surname list
            value = temp_list[n]
            pos = n - 1  # set pos to the left of value
            while pos >= 0 and value < temp_list[pos]:
                temp_list[pos + 1] = temp_list[pos]
                pos -= 1
            temp_list[pos + 1] = value
            return temp_list  # return sorted list of surnames

