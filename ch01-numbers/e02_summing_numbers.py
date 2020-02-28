#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2: mysum"""


def mysum(*numbers):
    """Accepts any number of numeric arguments as inputs.
Returns the sum of those numbers.
If invoked without any arguments, returns 0.
"""
    output = 0
    for number in numbers:
        output += number
    return output
