#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 4: even_odd_sums"""


def even_odd_sums(numbers):
    """Takes a list of numbers, and returns a two-element
list containing the sum of the even-indexed elements and the
sum of the odd-indexed elements.
"""
    return [sum(numbers[0::2]), sum(numbers[1::2])]
