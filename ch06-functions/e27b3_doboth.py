#!/usr/bin/env python3

"""Solution to chapter 6, exercise 27, beyond 3: doboth"""


def doboth(f1, f2):
    def inner(data):
        return f2(f1(data))
    return inner
