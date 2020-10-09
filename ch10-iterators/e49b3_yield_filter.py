#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49, beyond 3: yield_filter"""


def yield_filter(data, func):
    for one_item in data:
        if func(one_item):
            yield one_item
