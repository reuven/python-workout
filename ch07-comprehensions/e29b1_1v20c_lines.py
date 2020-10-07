#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 1: lines_with_1v20c"""


def lines_with_1v20c(filename):
    return [one_line
            for one_line in open(filename)
            if len(one_line) >= 20 and
            len(set('aeiou') & set(one_line)) >= 1]
