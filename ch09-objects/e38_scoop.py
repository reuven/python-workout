#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38: scoop"""


class Scoop():
    """Class representing a single scoop of ice cream.
The sole attribute is "flavor", a string.
"""

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    """Function that creates three scoops, puts them
in a list, and iterates over that list, printing the
flavors.
"""
    scoops = [Scoop('chocolate'),
              Scoop('vanilla'),
              Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)
