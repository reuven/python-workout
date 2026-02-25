#!/usr/bin/env python3
"""Solution to chapter 2, exercise 8, beyond 3: Longest word in a file"""


def longest_word(filename):
    """Given the name of a text file,
return the longest word in that file.
"""
    output = ''
    for one_line in open(filename):
        split_line=one_line.split()
        split_line.append(output)
        output=max(split_line)
    return output
