#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 5: plus_minus"""


def plus_minus(numbers):
    """Takes a list of numbers, and returns the result
of alternately adding and subtracting them.
"""

    if not numbers:
        return 0

    return numbers[0]+sum(numbers[1::2])-sum(numbers[2::2])
