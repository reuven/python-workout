#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 6: myzip"""


def myzip(*args):
    """Takes any number of iterables, returning
a list of tuples. The tuple at index n will contain
the items from index n in each iterable.  We can
assume that all of the iterables have the same length.
"""
    return [tuple(a[i] for a in args)
            for i in range(len(min(args, key=len)))]
