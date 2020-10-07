#!/usr/bin/env python3

"""Solution to chapter 7, exercise 31, beyond 1: funcfile"""


def funcfile(filename, func):
    return ' '.join(func(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())
