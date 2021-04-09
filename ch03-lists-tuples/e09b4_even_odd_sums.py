#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 4: even_odd_sums"""


def even_odd_sums(numbers):
    """Takes a list of numbers, and returns a two-element
list containing the sum of the even-indexed elements and the
sum of the odd-indexed elements.
"""
    evens = []
    odds = []

    for num in numbers[::2]:
        evens.append(num)

    for num in numbers[1::2]:
        odds.append(num)

    return [sum(evens), sum(odds)]
