#!/usr/bin/env python3
"""Solution to chapter 4, exercise 17: different_numbers"""


def how_many_different_numbers(numbers):
    """Takes a list of numbers as input.
Returns the number of different numbers in that list.
"""
    unique_numbers = set(numbers)
    return len(unique_numbers)
