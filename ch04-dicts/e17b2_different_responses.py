#!/usr/bin/env python3
"""Solution to chapter 4, exercise 17, beyond 2: different_responses"""


def different_responses(filename):
    return {one_line.split()[8]
            for one_line in open(filename)}
