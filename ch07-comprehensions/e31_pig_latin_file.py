#!/usr/bin/env python3

"""Solution to chapter 7, exercise 31: plfile"""


def plword(word):
    """Takes a string as input. It should be a single
word.  Returns a string, the input word translated into
Pig Latin.
"""
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def plfile(filename):
    """Takes a filename as input. Returns a string
containing the file's contents, with each word
translated into Pig Latin.
"""
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())
