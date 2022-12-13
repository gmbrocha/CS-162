# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/9/2022
# Description: Program allowing for creation of library items (books, albums, movies), patrons of the library as well as
# library objects themselves. Provides methods for each object type to get and amend attributes and lists containing
# those objects. Project involves class inheritance and composition - script provides examples for those topics.

class LibraryItem:
    """class defining LibraryItem objects and their methods"""

    def __init__(self, library_item_id, title):
        """initializes LibraryItem objects with item id and title parameters, also initializes
        checked out by and requested by parameters which hold Patron objects, location and date checked out"""
        self._library_item_id = library_item_id  # unique identifier for LibraryItem
        self._title = title  # not assumed to be unique, method to find items only used unique ids so this won't be a
        # problem unless a search for book title is required
        self._checked_out_by = None  # will hold a patron object
        self._requested_by = None  # will hold a patron object
        self._location = "ON_SHELF"  # current location with these values: ON_SHELF, CHECKED_OUT, ON_HOLD, ON_HOLD_SHELF
        self._date_checked_out = None  # hold integer date that patron checked out LibraryItem

    def get_location(self):
        """get method for LibraryItem location"""
        return self._location

    def set_location(self, new_loc):
        """set method for changing LibraryItem location"""
        self._location = new_loc

    def get_date_checked_out(self):
        """get method that returns LibraryItem date checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, current_date):
        """set method for changing LibraryItem date checked out"""
        self._date_checked_out = current_date

    def get_checked_out_by(self):
        """get method that returns patron who has checked out the LibraryItem"""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """set method to change the patron who was checked out the LibraryItem"""
        self._checked_out_by = patron

    def get_requested_by(self):
        """get method that returns patron who has requested LibraryItem"""
        return self._requested_by

    def set_requested_by(self, patron):
        """set method to change patron who has requested LibraryItem """
        self._requested_by = patron

    def get_library_item_id(self):
        """get method that returns id of LibraryItem"""
        return self._library_item_id

    def get_title(self):
        """get method that returns title of LibraryItem"""
        return self._title


class Patron:
    """class defining Patron objects and their methods"""

    def __init__(self, patron_id, name):
        """initializes Patron objects with patron id and name parameters"""
        self._patron_id = patron_id  # holds patron unique id
        self._name = name  # can't be assumed to be unique, method to find patrons only uses id's so this will not be an
        # issue unless need to ever search by name?
        self._checked_out_items = []  # list to hold LibraryItem objects that are currently checked out by patron
        self._fine_amount = 0  # this amount is allowed to go negative

    def get_fine_amount(self):
        """get method for patron's current fine amount"""
        return self._fine_amount

    def get_patron_id(self):
        """get method for patron id"""
        return self._patron_id

    def add_library_item(self, library_item):
        """adds library item to patron's checked out items list"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """removes library item from patron's checked out items list"""
        self._checked_out_items.remove(library_item)

    def get_checked_out_items(self):
        """get method that returns current patron checked out items list"""
        return self._checked_out_items

    def amend_fine(self, fine):
        """method to amend patrons fine amount"""
        self._fine_amount += fine


class Library:
    """class defining Library objects and their methods"""

    def __init__(self):
        """initializes Library objects and assigns parameters"""
        self._holdings = []  # will hold LibraryItem objects
        self._members = []  # will hold Patron objects
        self._current_date = 0  # current date for library, will be incremented with method increment_current_date

    def get_current_date(self):
        """get method to return Library current date, only used for debugging"""
        return self._current_date

    def get_holdings(self):
        """get method to return library holdings, only used for debugging"""
        return self._holdings

    def add_library_item(self, library_item):
        """adds library item to library's holdings list"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """adds patron to library members list"""
        self._members.append(patron)

    def lookup_library_item_from_id(self, item_id):
        """method to find item object by it's item id parameter"""
        in_library = None  # initialize in_library to hold boolean value after conditional checks for item below
        for lib_item in self._holdings:  # loop through LibraryItems in holdings list
            if lib_item.get_library_item_id() == item_id:  # check for item by id and set boolean
                in_library = True
                return lib_item  # return lib_item object
        if not in_library:  # if boolean is false, return None
            return None

    def lookup_patron_from_id(self, patron_id):
        """method to find patron by his/her patron id parameter"""
        is_member = None  # initialize is_member to hold boolean value after conditional checks for member below
        for member in self._members:  # loop through Patrons in library members list
            if member.get_patron_id() == patron_id:  # check for patron by id and set boolean
                is_member = True
                return member
        if not is_member:  # if boolean is false, return None
            return None

    def check_out_library_item(self, patron_id, item_id):
        """checks for valid item and patron, applies get and set methods for the item, and adds item to patron checked
        out items"""
        patron_ = self.lookup_patron_from_id(patron_id)  # store patron object from search method
        item_ = self.lookup_library_item_from_id(item_id)  # store LibraryItem object from search method
        if patron_ is None:
            print("patron not found")
        elif item_ is None:
            print("item not found")
        elif item_.get_location() == "CHECKED_OUT":  # check if LibraryItem is already checked out
            print("item already checked out")
        elif item_.get_location() == "ON_HOLD_SHELF":  # check if LibraryItem is on hold shelf
            print("item on hold by other patron")
        else:
            item_.set_checked_out_by(patron_)  # set LibraryItem attribute to patron object
            item_.set_date_checked_out(self._current_date)  # set LibraryItem attribute to the current date
            item_.set_location("CHECKED_OUT")  # set LibraryItem location as checked out
            if item_.get_requested_by() == patron_:  # if the LibraryItem was already requested by this patron, change
                # the item's attribute back to None
                item_.set_requested_by(None)
            patron_.add_library_item(item_)  # add LibraryItem object to patron list of checked out items
            return "check out successful"

    def return_library_item(self, item_id):
        """checks for item, applies get and set methods for location of LibraryItem"""
        item_ = self.lookup_library_item_from_id(item_id)  # store LibraryItem object from search method
        if item_ is None:
            return "item not found"
        elif item_.get_location == "ON_SHELF":  # check if item already exists on the shelf
            return "item already in library"
        else:
            item_.get_checked_out_by().remove_library_item(item_)  # remove LibraryItem from patrons checked out items
            if item_.get_requested_by() is None:  # conditional to see if the LibraryItem was requested by another
                # patron while it was already checked out, if it wasn't, place on_shelf, otherwise put on_hold_shelf
                item_.set_location("ON_SHELF")
            else:
                item_.set_location("ON_HOLD_SHELF")
            item_.set_checked_out_by(None)  # set None for the LibraryItem attribute checked_out_by
            return "return successful"

    def request_library_item(self, patron_id, item_id):
        """checks for item, whether it's on hold, applies get and set methods for location of LibraryItem"""
        patron_ = self.lookup_patron_from_id(patron_id)  # store LibraryItem object from search method
        item_ = self.lookup_library_item_from_id(item_id)  # store patron object from search method
        if patron_ is None:
            return "patron not found"
        elif item_ is None:
            return "item not found"
        elif item_.get_requested_by() is not None:  # check if item was already requested by another patron
            return "item already on hold"
        else:
            item_.set_requested_by(patron_)  # set LibraryItem requested_by attribute to the patron object
            if item_.get_location() == "ON_SHELF":  # this conditional checks whether the LibraryItem object is on_shelf
                # or checked_out, and sets the new location accordingly
                item_.set_location("ON_HOLD_SHELF")
            elif item_.get_location() == "CHECKED_OUT":
                item_.set_location("ON_HOLD")

    def pay_fine(self, patron_id, amount):
        """uses amend fine method to deduct amount pass from patron's fine"""
        patron_ = self.lookup_patron_from_id(patron_id)  # store patron object from search method
        if patron_ is None:
            print("patron not found")
        else:  # if patron object exists, amend patron object's fine amount attribute by how much paid
            amount *= -1  # make amount negative to decrement the fine amount
            patron_.amend_fine(amount)
            return "payment successful"

    def increment_current_date(self):
        """increments current date and checks it item is overdue and increases patron's fine accordingly"""
        self._current_date += 1  # increment Library object attribute current_date by 1
        for item in self._holdings:  # iterate through LibraryItem objects in Library holdings list
            if item.get_location() == "CHECKED_OUT" or item.get_location() == "ON_HOLD":  # if LibraryItem object
                # location is either checked_out or on_hold (requested but already checked out) conditional passes
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():  # check if
                    # LibraryItem is overdue by calling methods date_checked_out and max check_out_length
                    item.get_checked_out_by().amend_fine(.10)  # add .10 to patron object's fine


class Book(LibraryItem):
    """defines Book items from the parent class LibraryItem"""

    def __init__(self, library_item_id, title, author):
        """initializes Book objects of superclass LibraryItem and parameters"""
        super().__init__(library_item_id, title)  # call init method of superclass LibraryItem
        self._library_item_id = library_item_id  # Str id of Book object
        self._title = title  # Str title of Book object
        self._author = author  # Str author of Book object

    def get_author(self):
        """get method to return author parameter"""
        return self._author

    @staticmethod
    def get_check_out_length():
        """get method to return max check out length before item overdue"""
        return 21


class Album(LibraryItem):
    """defines Album items from the parent class LibraryItem"""

    def __init__(self, library_item_id, title, artist):
        """initializes Album objects of superclass LibraryItem and parameters"""
        super().__init__(library_item_id, title)  # call init method of superclass LibraryItem
        self._library_item_id = library_item_id  # Str id of Album object
        self._title = title  # Str title of Album object
        self._artist = artist  # Str artist of Album object

    def get_artist(self):
        """get method to return artist parameter"""
        return self._artist

    @staticmethod
    def get_check_out_length():
        """get method to return max check out length before item overdue"""
        return 14


class Movie(LibraryItem):
    """defines Movie items from the parent class LibraryItem"""

    def __init__(self, library_item_id, title, director):
        """initializes Movie objects of superclass LibraryItem and parameters"""
        super().__init__(library_item_id, title)  # call init method of superclass LibraryItem
        self._library_item_id = library_item_id  # Str id of Movie object
        self._title = title  # Str title of Movie object
        self._director = director  # Str director of Movie object

    def get_director(self):
        """get method that returns director parameter"""
        return self._director

    @staticmethod
    def get_check_out_length():
        """get method to return max check out length before item overdue"""
        return 7


def main():
    """Function that runs as a script but not imported to other programs."""
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(m1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    for _ in range(7):
        lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item("abc", "567")
    lib.request_library_item("bcd", "567")
    for _ in range(57):
        lib.increment_current_date()  # 57 days pass
    p1_fine = p1.get_fine_amount()
    print(p1.get_fine_amount())
    lib.pay_fine("abc", p1_fine)
    lib.return_library_item("567")

    print(p1.get_fine_amount())
    print(p2.get_fine_amount())


if __name__ == '__main__':  # IF statement that allows prevents this main() function from running outside this program.
    main()
