#!/usr/bin/env python3

"""Solution to chapter 9, exercise 39: bowl"""


class Scoop():
    """Class representing a single scoop of ice cream.
The sole attribute is "flavor", a string.
"""

    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    """Class representing a bowl of ice cream.

The "scoops" attribute is a list, containing scoops.
You can add one or more scoops with the "add_scoops" method.
"""

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        """Add one or more scoops to the bowl"""
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
