#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(sorted(a_dictionary.keys()))
    for i in dict_keys:
        print("{}: {}".format(i, a_dictionary[i]))
