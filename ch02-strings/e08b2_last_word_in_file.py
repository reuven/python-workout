#!/usr/bin/env python3
"""Solution to chapter 2, exercise 8, beyond 2: Last word (alphabetically) in a file"""


def last_word_alphabetically(filename):
    """Given the name of a text file,
return the word that comes last (alphabetically)
in that file.
"""
    output = ''
    for one_line in open(filename):
        split_line=one_line.split()
        split_line.append(output)
        output=max(split_line)
    return output
