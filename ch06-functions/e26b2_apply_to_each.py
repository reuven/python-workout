#!/usr/bin/env python3

"""Solution to chapter 6, exercise 26, beyond 2: apply_to_each"""


def apply_to_each(f, seq):

    return [f(one_item)
            for one_item in seq]
