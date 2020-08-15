#!/usr/bin/env python3
"""Solution to chapter 3, exercise 10, beyond 3: combine_dicts"""


def combine_dicts(*args):
    """Return a dict, the result of combining all
elements of args (which should be dicts).  If a key
occurs in more than one, then the value should be a list
containing all values from the arguments.
"""
    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output
