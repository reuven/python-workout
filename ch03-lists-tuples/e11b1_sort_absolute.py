#!/usr/bin/env python3
"""Solution to chapter 3, exercise 11, beyond 1: sort_absolute"""


def sort_absolute(numbers):
    """Given an iterable of numbers, return
a list of those numbers sorted by absolute value.
"""
    return sorted(numbers, key=abs)
