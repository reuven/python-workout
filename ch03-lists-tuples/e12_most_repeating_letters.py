#!/usr/bin/env python3
"""Solution to chapter 3, exercise 12: most_repeating_word"""

from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    """Given a non-empty string, counts how
many times each letter appears in the string,
and returns an integer indicating how often
the most common letter appears."""
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    """Given a list of non-empty strings (words),
returns the word containing at least one letter that repeats
more often than any letter in any other word.

Because sorting in Python is stable, if multiple words have
the same count, then the first will be returned."""
    return max(words, key=most_repeating_letter_count)
