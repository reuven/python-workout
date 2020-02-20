#!/usr/bin/env python3
"""Solution to chapter 5, exercise 21: longest_word"""


import os


def find_longest_word(filename):
    """Given a filename, return the longest word in the file."""
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word


def find_all_longest_words(dirname):
    """Given a directory name, return a dict in which the keys
are filenames in the directory and the values are
the strings -- the longest word in each file."""
    return {filename: find_longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, filename))}
