#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 1: mysum with start"""


def mysum(numbers, start=0):
    """Accepts any number of numeric arguments as inputs.
Returns the sum of those numbers, plus the value of "start",
which defaults to 0.
"""
    output = start
    for number in numbers:
        output += number
    return output
