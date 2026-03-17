#!/usr/bin/env python3

"""Solution to chapter 8, exercise 36, beyond 3: fromkeys_func"""


def fromkeys_func(s, func):
    return {key: func(key) for key in s}
