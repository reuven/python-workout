#!/usr/bin/env python3

"""Solution to chapter 7, exercise 33: transform_values"""


def transform_values(func, a_dict):
    """Takes two arguments, a function and a dict.
Returns a dict in which the keys are the original
dict's keys, but the values are the result of invoking
the function on each original value.
"""
    return {key: func(value)
            for key, value in a_dict.items()}
