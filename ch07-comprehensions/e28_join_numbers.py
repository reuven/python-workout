#!/usr/bin/env python3

"""Solution to chapter 7, exercise 28: join_numbers"""


def join_numbers(numbers):
    """Takes an iterable of numbers as input.
Output is a string containing the numbers in that iterable,
separated by commas.
"""
    return ','.join(str(number)
                    for number in numbers)
