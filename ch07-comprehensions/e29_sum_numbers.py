#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29: sum_numbers"""


def sum_numbers(numbers):
    """Takes a string containing space-separated words.
Output is an integer, the sum of those words that can
be turned into integers.
"""
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())
