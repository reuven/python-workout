#!/usr/bin/env python3

"""Solution to chapter 10, exercise 50, beyond 1: myzip"""


def myzip(*args):
    for i in range(len(min(args, key=len))):
        yield tuple(one_arg[i]
                    for one_arg in args)
