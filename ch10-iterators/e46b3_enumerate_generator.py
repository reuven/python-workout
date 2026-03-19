#!/usr/bin/env python3

"""Solution to chapter 10, exercise 46, beyond 3: enumerate_generator"""


def my_enumerate(data, start=0):

    for index,one_item in zip(range(start,start+len(data)), data):
        yield (index, one_item)
