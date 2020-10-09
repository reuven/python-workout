#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5, beyond 1: Pig Latin, handle capitalization"""

import string


def pig_latin_capitalized(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string.

If the original word is capitalized, then the output
should be, as well.
"""
    if word[0].lower() in 'aeiou':
        output = f'{word}way'
    else:
        output = f'{word[1:]}{word[0]}ay'

    if word[0] in string.ascii_uppercase:
        output = output.capitalize()

    return output
