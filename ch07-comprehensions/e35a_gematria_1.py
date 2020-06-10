#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35a: gematria_dict"""

import string


def gematria_dict():
    """Function that returns a dictionary of ASCII values
for all lowercase letters. The keys are the letters, and
the values are the numbers, starting with 1 for 'a'.
"""
    return {char: index
            for index, char in enumerate(string.ascii_lowercase, 1)}
