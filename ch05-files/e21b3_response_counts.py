#!/usr/bin/env python3
"""Solution to chapter 5, exercise 21, beyond 3: response_counts"""


from collections import Counter


def response_counts(filename):
    output = Counter()

    for one_line in open(filename):
        output[one_line.split()[8]] += 1

    return output
