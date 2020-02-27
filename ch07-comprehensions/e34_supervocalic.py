#!/usr/bin/env python3

"""Solution to chapter 7, exercise 34: get_sv"""


def get_sv(filename):
    """Given a filename (string) as input,
this function returns a set of all words
in which all five vowels can be found.
"""
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
            for word in open(filename)
            if vowels < set(word.lower())}
