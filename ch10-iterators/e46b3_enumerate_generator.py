#!/usr/bin/env python3

"""Solution to chapter 10, exercise 46, beyond 3: enumerate_generator"""


def my_enumerate(data, start=0):
    index = start

    for one_item in data:
        yield (index, one_item)
        index += 1
