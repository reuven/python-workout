#!/usr/bin/env python3
"""Solution to chapter 3, exercise 10, beyond 2: sum_numeric"""


def sum_numeric(items):
    """Sum all items, assuming that they
are integers or can be turned into integers.
"""
    total = 0

    for item in items:
        try:
            total += int(item)
        except ValueError:
            pass
    return total
