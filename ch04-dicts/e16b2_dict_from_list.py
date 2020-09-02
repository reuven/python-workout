#!/usr/bin/env python3
"""Solution to chapter 4, exercise 16, beyond 2: dict_from_list"""


def dict_from_list(*args):
    if len(args) % 2:
        raise ValueError('Need an even number of args')

    output = {}

    while args:
        output[args[0]] = args[1]
        args = args[2:]

    return output
