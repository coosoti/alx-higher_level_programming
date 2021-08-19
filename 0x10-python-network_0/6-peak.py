#!/usr/bin/python3
"""Find the highest value in an integer"""


def find_peak(list_of_integers):
    """Find highest value in a list of unsorted integers"""

    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
