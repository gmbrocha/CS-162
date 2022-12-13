# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/08/2022
# Description: script with 2 classes - a Node class defining node objects with a data attribute as well as a next
# attribute which will reference another node object in a linked list. The second class is the LinkedList class which
# initializes with a head attribute, that is 'index 0' of the linked list. The class also provides methods to: check if
# the linked list object is empty, add nodes (by instantiating Node objects with a passed value), remove nodes (by
# parsing the linked list for values matching the passed value), checking if the list contains a value in any of its
# objects, inserting node objects into precise places within the linked list (by using a passed position argument as an
# 'index' for the desired insertion), reverse the linked list objects without changing the data values contained (only
# by changing the .next reference for each object), as well as simple get method for retrieving the head object of the
# linked list. All methods achieve list sorting and searching through function/method recursion, rather than loops.


class Node:
    """defines creation of Node objects that will be associated with one another in the class LinkedList; each of these
    Nodes will contain data and a reference data member to the next node in a LinkedList"""

    def __init__(self, data):
        self.data = data  # stores the data value for each node object
        self.next = None  # data member that will hold a reference to the next Node object in a LinkedList


class LinkedList:
    """defines creation of class LinkedList objects that will be abstract, non-contiguous lists containing Node objects
    that both have data and a reference to the following object in the list; methods are defined below to: add and
    remove new Node objects to the list, insert objects at passed 'index', check if list contains object with a passed
    value as it's data, reverse the objects in the list, return a plain python list of the object's values in the
    non-contiguous list, as well as a get method to return the head value (first object) from the LinkedList object"""

    def __init__(self):
        self._head = None  # initialize the head of the linked list object to None

    def is_empty(self):
        """returns True if the LinkedList is empty; False otherwise"""

        return self._head is None

    def add(self, value, current=None):
        """adds Node objects to LinkedList; sets the head value to Node class call and passes value if the LinkedList is
         empty; if not empty - performs a function recursion to find the last Node object in the LinkedList and
         instantiates a new Node object into the current object's .next parameter"""

        if self.is_empty():  # this sets head as a Node class call, passing value, if head is empty
            self._head = Node(value)
        else:
            if current is None:  # set initial value for current parameter as head object
                current = self._head
            if current.next is not None:  # check current.next parameter of object (beginning at head) for None
                self.add(value, current.next)  # if parameter has a value (reference to next Node), recurse
            elif current.next is None:  # once the object is found with .next parameter as None (last in the 'list') set
                # the .next parameter to a Node class call and pass new_value for data
                current.next = Node(value)
                return None

    def remove(self, value, current=None, previous=None):
        """remove Node objects from LinkedList by searching object's data values for the value passed by the method
        call, if value found remove the associated object"""

        if self.is_empty():  # provide None return if the method is called on an empty list
            return None

        if current is None:  # initial set of current to self._head if None
            current = self._head
            if current.data == value:  # should cover situation where the first object contains value, otherwise, the
                # next conditional to evaluate to true will be the elif below - and previous won't have been assigned
                self._head = current.next
                return None

        if current.data != value:  # check .data of current object for passed value equivalence
            previous = current
            current = current.next
            if current is None:  # if current (current.next) is None, this is the end of the list; value not found
                return None
        elif current.data == value:  # if current.data is equal to value then set previous.next to current.next which
            # is the value directly to the right of current; effectively removes current object from LinkedList
            previous.next = current.next
            return None
        self.remove(value, current, previous)  # recursive method call

    def contains(self, value, current=None):
        """check the LinkedList for passed data argument a_val and return either True or False if the list
        does or does not contain a_val, respectively; recursively uses itself to iterate the list and check for a_val
        equality of each object's data member, data"""

        if self.is_empty():  # if head is empty there will be nothing to compare so return False
            return False

        if current is None:  # set initial value for current from default value to head value
            current = self._head
        if current.next is not None:  # if .next value of object is not None then check for a_val data equality
            if current.data == value:  # if equal return True
                return True
            elif current.data != value:  # if .next is not equal to a_val, recurse and pass the .next object
                self.contains(value, current.next)
        elif current.next is None:  # if .next is None, check last value for equality; if current.data not a_val, the
            # value is not in the list, return False
            if current.data == value:  # need this to check last object for equality
                return True
            else:
                return False
        recurse = self.contains(value, current.next)  # recursive call set to recurse identifier
        if recurse is True:  # if returned value stored in recurse is True, return True
            return True
        elif recurse is False:  # if returned value stored in recurse is False, return False
            return False

    def insert(self, value, position, current=None, previous=None, pos=0):
        """insert Node objects (by value) into the LinkedList at a position argument; analogous to indices in a standard
        python list; will traverse list until the 'index' is found and place a Node object between the previous and
        current.next objects"""

        if current is None:  # initialize current to the list head value
            current = self._head
        elif position == 0:  # if position passed is 0, set current to a class Node call and pass value
            current = Node(value)
            current.next = self._head  # set the .next data member of the object to original head
            self._head = current  # change the head to the new current object
            return None
        elif position != 0:  # for all other cases where the pass position is not 0
            previous = current  # set previous to the current object
            current = current.next  # set current to the current objects next data member
            if current is None:  # if current (.next) is None, at the end of list
                previous.next = Node(value)  # set previous.next to a new Node class call and pass value
                return None
            elif position == pos:  # if position passed is not 0, and current is not None, AND position is equal to pos
                previous.next = Node(value)  # previous.next attribute set to new Node class call and pass value
                previous.next.next = current  # previous.next now refers to that object, .next again to set proper
                # reference to next node
                return None
        self.insert(value, position, current, previous, pos + 1)

    def reverse(self, current=None, temp_list=None):
        """method that reverses the order of objects in the LinkedList; creates a temp_list to hold the Node object
        items, then reverses that list by slicing, and then reassigns the head value as well as each .next value by
        the object in the reversed list"""

        if self.is_empty():  # if list is empty, return None
            return None

        if current is None and temp_list is None:  # if current is None, initialize its value as self._head
            current = self._head
            temp_list = []  # set initial value for temp_list from default

        if current.next is not None:  # if .next value is not None, append current to temp_list and then recurse
            temp_list.append(current)
            self.reverse(current.next, temp_list)
        else:  # when None is reached, the end of the list is found
            temp_list.append(current)  # add last object to temp_list
            rev_list = temp_list[::-1]  # reverse by slicing

            def reverse_rec(current_=None, a_list=None, index=0):  # second reverse recursive function to pull the
                # objects from the reversed list and set their .next reference accordingly
                if current_ is None:  # if current_ is None (first iteration), do:
                    a_list = rev_list  # set a_list as the rev_list from above
                    current_ = a_list[index]  # set current_ as a_list[0] (first value in a_list)
                    self._head = current_  # set the head value as current_
                if current_ is not None:  # after previous conditional, perform this with recursion
                    if index == len(a_list) - 1:  # set base case to exit
                        current_.next = None  # upon recursion exit, set last Node object .next value to None
                        return
                    else:
                        current_.next = a_list[index + 1]  # set .next to next index value in reversed list
                        reverse_rec(current_.next, a_list, index + 1)  # recursive call to helper function
            reverse_rec()  # call the recursive helper function

    def to_plain_list(self, current=None, temp_list=None):
        """method that uses recursion to iterate through the non-contiguous list and append the data values to a regular
        python list and returns that list to the method call"""

        if self.is_empty():  # if head is empty return None immediately from function
            return None

        if temp_list is None:  # initialize temp list as empty and set current to head object to begin
            temp_list = []
            current = self._head
        temp_list.append(current.data)  # append current object .data to temp_list
        if current.next is None:
            return temp_list  # if current.next is None; end of list - return temp_list
        self.to_plain_list(current.next, temp_list)  # recursive call to function with .next object and temp_list
        return temp_list

    def get_head(self):
        """get method to return Node object at head of list"""

        return self._head  # return Node object at 'index 0' of the linked list
