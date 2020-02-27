#!/usr/bin/env python3

"""Solution to chapter 7, exercise 32: flipped_dict"""


def flipped_dict(a_dict):
    """Gets a dict as an argument.
Returns a dict as output. The output dict's keys
are the input dict's values, and vice versa.
"""
    return {value: key
            for key, value in a_dict.items()}
