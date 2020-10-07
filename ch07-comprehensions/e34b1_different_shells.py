#!/usr/bin/env python3

"""Solution to chapter 7, exercise 34, beyond 1: different_shells"""


def different_shells(filename):
    return {one_line.split(':')[-1].strip()
            for one_line in open(filename)
            if not one_line.startswith(('\n', '#'))}
