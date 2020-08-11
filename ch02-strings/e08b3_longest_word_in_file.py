#!/usr/bin/env python3
"""Solution to chapter 2, exercise 8, beyond 3: Longest word in a file"""


def longest_word(filename):
    """Given the name of a text file,
return the longest word in that file.
"""
    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output
