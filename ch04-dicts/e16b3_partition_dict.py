#!/usr/bin/env python3
"""Solution to chapter 4, exercise 16, beyond 3: partition_dict"""


def partition_dict(d, f):
    output_true = {}
    output_false = {}

    for key, value in d.items():
        if f(key, value):
            output_true[key] = value
        else:
            output_false[key] = value

    return output_true, output_false
