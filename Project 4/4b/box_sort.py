# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/18/2022
# Description: Defines class that instantiates Box objects with length, width, and height; provides methods to evaluate
#   volume, and to get length, width, height; defines an insertion sort function that sorts an input list of Box objects
#   by respective volume (descending)


class Box:
    """instantiates box objects and assigns length, width, and height parameters based on input"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """returns the volume of a Box object"""
        return self._length * self._width * self._height

    def get_length(self):
        """get method that returns length of Box object"""
        return self._length

    def get_width(self):
        """get method that returns width of Box object"""
        return self._width

    def get_height(self):
        """get method that returns height of Box object"""
        return self._height


def box_sort(b_list):
    """insertion sort that sorts input list of Box objects by volume (descending)"""
    for index in range(1, len(b_list)):
        value = b_list[index].volume()
        temp_box = b_list[index]  # added because value is simple the volume of the box object - after inside loop
        # executes then b_list[pos + 1] must equal an object and not just it's volume
        pos = index - 1
        while pos >= 0 and b_list[pos].volume() < value:  # check value on the right to value on the left, if volume
            # of box object on left is less than volume of box on right, execute this loop to change right box to that
            # of left box
            b_list[pos + 1] = b_list[pos]
            pos -= 1  # decrement pos so that the loop will continue moving to the left and switching the value on the
            # right until pos is -1 or volume on the right is actually greater than box volume on the left
        b_list[pos + 1] = temp_box


# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# b4 = Box(5, 1.7, 50)
# b5 = Box(1, 2, 1)
# box_list = [b1, b2, b3, b4, b5]
# print(box_list[0].volume(), box_list[1].volume(), box_list[2].volume(), box_list[3].volume(), box_list[4].volume())
# box_sort(box_list)
# print(box_list[0].volume(), box_list[1].volume(), box_list[2].volume(), box_list[3].volume(), box_list[4].volume())


