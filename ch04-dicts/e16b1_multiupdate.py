#!/usr/bin/env python3
"""Solution to chapter 4, exercise 16, beyond 1: multi_update"""


def multi_update(*args):
    output = {}

    for one_dict in args:
        output.update(one_dict)

    return output
