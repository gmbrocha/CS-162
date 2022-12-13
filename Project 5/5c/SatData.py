# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/23/2022
# Description: Class SatData which defines creation of SatData objects; instantiates objects with private data member
#     dictionaries to hold json information; provides method to search, and retrieve information associated with the
#     input dbns that are sorted; writes information to output.csv

import json


class SatData:
    """defines creation of SatData objects; instantiates them with private data member dictionaries holding json
    information; provides method to search, and retrieve information associated with the input dbns that are sorted;
    writes that information to output.csv"""

    def __init__(self):
        """instantiate SatData objects and initialize a single private data member dictionary to store json target"""
        self._sat_dict = {}
        with open("sat.json", "r") as infile:
            self._sat_dict = json.load(infile)

    def save_as_csv(self, dbn_list):
        """method that accepts a list of database numbers as strings; sorts the list; searches self._sat_dict for items
        with input dbns and writes to output.csv the data associated with that dbn (sorted by dbn)"""
        # first  for loop structure will write the column headers #
        with open("output.csv", "w") as outfile:
            for n in range(8, len(self._sat_dict["meta"]["view"]["columns"]) - 1):  # range start 8 for headers
                outfile.write(self._sat_dict["meta"]["view"]["columns"][n]["name"] + ",")
            outfile.write(self._sat_dict["meta"]["view"]["columns"][len(self._sat_dict["meta"]["view"]["columns"]) - 1]
                          ["name"] + "\n")  # separate this from loop to avoid comma at end of row

        # second loop struction sorts the input list
            for n in range(1, len(dbn_list)):  # insertion sort the list by dbn
                value = dbn_list[n]
                pos = n - 1
                while pos >= 0 and value < dbn_list[pos]:
                    dbn_list[pos + 1] = dbn_list[pos]
                    pos -= 1
                dbn_list[pos + 1] = value

        # third loop structure searches the json dict for dbn inputs and writes values associated with them to
            # output.txt
            for n in range(0, len(self._sat_dict["data"]) - 1):
                for dbn in dbn_list:
                    if dbn in self._sat_dict["data"][n]:
                        count = 6
                        while count > 1:
                            if "," in str(self._sat_dict["data"][n][len(self._sat_dict["data"][n]) - count]):
                                outfile.write('"' + str(self._sat_dict["data"][n][len(self._sat_dict["data"][n])
                                                                                  - count]) + '",')
                            else:
                                outfile.write(str(self._sat_dict["data"][n][len(self._sat_dict["data"][n])
                                                                            - count]) + ',')
                            count -= 1
                        outfile.write(str(self._sat_dict["data"][n][13]) + "\n")

