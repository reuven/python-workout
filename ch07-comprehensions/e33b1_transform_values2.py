#!/usr/bin/env python3

"""Solution to chapter 7, exercise 33, beyond 1: transform_values2"""


def transform_values2(func1, func2, a_dict):
    return {key: func(value)
            for key, value in a_dict.items()
            if func2(key, value)}
