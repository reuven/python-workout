#!/usr/bin/env python3

"""Solution to chapter 7, exercise 34, beyond 2: word_lengths"""


def word_lengths(filename):
    return {len(one_word)
            for one_line in open(filename)
            for one_word in one_line.split()}
