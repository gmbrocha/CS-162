# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/23/2022
# Description:

import json


class DuplicateNameError(Exception):
    pass


class Pet:
    """"""

    def __init__(self, name, species, owner):
        self._name = name
        self._species = species
        self._owner = owner


class NeighborhoodPets:
    """"""

    def __init__(self):
        """"""
        self._pets = []

    def add_pet(self, name, species, owner):
        """"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:
                raise DuplicateNameError
        self._pets.append({"name": name, "species": species, "owner": owner})

    def delete_pet(self, name):
        """"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:
                self._pets.remove(pet_dict)

    def get_owner(self, name):
        """"""
        for pet_dict in self._pets:
            if pet_dict["name"] == name:
                return pet_dict["owner"]

    def save_as_json(self, file_name):
        """"""
        with open(file_name, "w") as outfile:
            json.dump(self._pets, outfile)

    def read_json(self, file_name):
        """"""
        with open(file_name, "r") as infile:
            self._pets = json.load(infile)

    def get_all_species(self):
        """"""
        temp_set = set()
        for pet_dict in self._pets:
            temp_set.add(pet_dict["species"])
        return temp_set


np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
    np.add_pet("Man", "lizard", "Brochard")
    np.add_pet("Biyrd", "bird", "Monica")
    np.add_pet("Manbearpig", "unknown", "Gore")
except DuplicateNameError:
    print("That name is already taken.")

np.save_as_json("other_pets.json")
