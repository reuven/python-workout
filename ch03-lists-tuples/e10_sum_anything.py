#!/usr/bin/env python3
"""Solution to chapter 3, exercise 10: mysum"""


def mysum(*items):
    """Sum the passed arguments, which should be of the same type.
The arguments should handle the + operator.
If passed no arguments, then return an empty tuple.
"""
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output
