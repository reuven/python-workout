#!/usr/bin/env python3
"""Solution to chapter 3, exercise 11, beyond 2: sort_by_vowel_count"""


def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


def sort_by_vowel_count(words):
    """Given a list of strings (words), return
a list of those words sorted by the number of vowels
they contain.
"""
    return sorted(words, key=by_vowel_count)
