#!/usr/bin/env python3

"""Solution to chapter 8, exercise 36, beyond 3: fromkeys_func"""


def fromkeys_func(s, func):
    output = {}

    for one_item in s:
        output[one_item] = func(one_item)

    return output
