#!/usr/bin/env python3

"""Solution to chapter 7, exercise 28, beyond 3: reverse_words"""


def reverse_words(filename):
    return [' '.join(reversed(one_line.split()))
            for one_line in open(filename)]
