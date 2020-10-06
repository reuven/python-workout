#!/usr/bin/env python3
"""Solution to chapter 6, exercise 25, beyond 2: factorialish"""


def factorialish(*args):
    if not args:
        return 0

    total = args[0]
    for one_number in args[1:]:
        total *= one_number

    return total
