#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5: pig_latin"""


def pig_latin(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string.
"""
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'
