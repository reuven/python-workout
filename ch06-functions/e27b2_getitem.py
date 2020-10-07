#!/usr/bin/env python3

"""Solution to chapter 6, exercise 27, beyond 2: getitem"""


def getitem(index):
    def inner(data):
        return data[index]
    return inner
