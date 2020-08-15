#!/usr/bin/env python3
"""Solution to chapter 3, exercise 10, beyond 1: mysum_bigger_than"""


def mysum_bigger_than(threshold, *items):
    """Sum items, which should be of the same type.
Ignore any below the value of threshold.
The arguments should handle the + operator.
If passed no arguments, then return an empty tuple.
"""
    if not items:
        return items
    output = 0
    for item in items:
        if item > threshold:
            output += item
    return output
