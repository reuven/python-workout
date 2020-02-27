#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29: flatten"""


def flatten(mylist):
    """Expects to get a nested list (a list of lists)
as input. Returns a flattened list, containing the
elements of mylist in order, as output.
"""
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]
