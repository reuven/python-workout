#!/usr/bin/env python3
"""Solution to chapter 4, exercise 15, beyond 3: word lengths"""

from collections import defaultdict


def word_lengths(filename):
    output = defaultdict(int)

    for one_line in open(filename):
        for one_word in one_line.split():
            output[len(one_word)] += 1

    return output
