#!/usr/bin/env python3
"""Solution to chapter 2, exercise 7, beyond 1: Ubbi Dubbi with capitals"""

import string


def ubbi_dubbi_caps(word):
    """Ask the user to enter a word,
and return the word's translation into Ubbi Dubbi.
If the input word is capitalized, then the output
word should be, too.
"""
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    if word[0] in string.ascii_uppercase:
        output[0] = output[0].capitalize()

    return ''.join(output)
