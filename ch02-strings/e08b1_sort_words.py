#!/usr/bin/env python3
"""Solution to chapter 2, exercise 8, beyond 1: Sort words"""


def sort_words(s):
    """Given a string containing comma-separated
words, return a string with the same words, separated
by commas, but sorted.
"""

    return ', '.join(one_word
                     for one_word in sorted(s.split()))
