# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/24/2022
# Description: Class defining creation of pets list; adding and removing pets; get methods for owner and set of species;
# provides methods to write and read pets lists to and from json files

import json


class DuplicateNameError(Exception):
    """user defined exception for duplicate pet name error"""
    pass


class NeighborhoodPets:
    """Class defining creation of pets list with each pet having parameters name, species, and owner; provides
    method to add pets to list as dictionaries; provides method to delete pet dicts and to get owner by name;
    provides methods to write pets list to json as well as read a new pet list from json stored previously"""

    def __init__(self):
        """instantiates NeighborhoodPets objects and creates an empty pet list as the single private data member"""
        self._pets = []  # create empty list to hold pets

    def add_pet(self, name, species, owner):
        """adds pet dict (each dict is a single pet) to pets list with name, species, and owner parameters; raises
        duplicateNameError if the name of the pet already exists in the list"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:  # check pet_dicts in pets list for parameter name already existing; raise
                # exception if it does
                raise DuplicateNameError
        self._pets.append({"name": name, "species": species, "owner": owner})  # append pet dict with keys name, species
        # and owner to pets list

    def delete_pet(self, name):
        """check pet dicts in pets list for parameter name and remove that from pets list"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:
                self._pets.remove(pet_dict)

    def get_owner(self, name):
        """get method that returns pet owner by single parameter pet name"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:
                return pet_dict["owner"]

    def save_as_json(self, file_name):
        """opens parameter file_name (as string with json extension) and writes pets list to file"""
        with open(file_name, "w") as outfile:
            json.dump(self._pets, outfile)

    def read_json(self, file_name):
        """opens parameter file_name (as string with json extension) and reads new pets list previous save_as_json"""
        with open(file_name, "r") as infile:
            self._pets = json.load(infile)

    def get_all_species(self):
        """get method to return a set containing all species in pets list"""
        temp_set = set()  # create temp set to hold species
        for pet_dict in self._pets:
            temp_set.add(pet_dict["species"])  # add species referenced with species key to set, adds only if species
            # not in set already
        return temp_set

