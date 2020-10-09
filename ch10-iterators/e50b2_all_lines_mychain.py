#!/usr/bin/env python3

"""Solution to chapter 10, exercise 50, beyond 2: all_lines_mychain"""


def mychain(*args):
    for arg in args:
        for item in arg:
            yield item


def all_lines(path):
    return mychain(*(open(os.path.join(path, filename))
                     for filename in os.listdir(path)
                     if os.path.isfile(os.path.join(path, filename))))
