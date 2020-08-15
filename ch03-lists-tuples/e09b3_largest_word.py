#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 3: Longest word in file-like"""


def longest_word(f):
    """Takes a file-like object, and returns the longest
word it finds.
"""
    longest_word = ''

    for one_line in f:
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word

    return longest_word
