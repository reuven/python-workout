#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 2: mean"""


def mean(numbers):
    """Accepts a non-empty list of numbers.

Returns the mean of those numbers.
"""
    return sum(numbers) / len(numbers)
