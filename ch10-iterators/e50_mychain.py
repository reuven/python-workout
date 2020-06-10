#!/usr/bin/env python3

"""Solution to chapter 10, exercise 50: mychain"""


def mychain(*args):
    """Generator that takes any number of iterables
as arguments. It yields, one at a time, each of the
elements of each iterable.

It is similar to itertools.chain.
"""
    for arg in args:
        for item in arg:
            yield item
