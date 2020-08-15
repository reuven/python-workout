#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 2: Largest anything"""


def largest(s):
    """Takes a sequence, and returns the largest
element (as defined by >) from the sequence.
"""
    if not s:
        return None

    output = s[0]

    for one_item in s[1:]:
        if one_item > output:
            output = one_item

    return output
