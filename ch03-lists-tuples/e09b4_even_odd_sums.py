#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 4: even_odd_sums"""


def even_odd_sums(numbers):
    """Takes a list of numbers, and returns a two-element
list containing the sum of the even elements and the
sum of the odd elements.
"""
    evens = []
    odds = []

    for one_number in numbers:
        if one_number % 2:
            odds.append(one_number)
        else:
            evens.append(one_number)

    return [sum(evens), sum(odds)]
