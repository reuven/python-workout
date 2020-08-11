#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5, beyond 3: Pig Latin, different vowels"""


def pig_latin_multivowels(word):
    """Our test for moving the
first letter to the end is whether
the word contains two or more different vowels.
"""
    number_of_vowels = len(set(word) & set('aeiou'))

    if number_of_vowels > 1:
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'
