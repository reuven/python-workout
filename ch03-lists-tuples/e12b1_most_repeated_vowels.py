#!/usr/bin/env python3
"""Solution to chapter 3, exercise 12, beyond 1: most_repeating_vowels"""

from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_vowel_count(word):
    vowels_in_word = ''
    for one_character in word.lower():
        if one_character in 'aeiou':
            vowels_in_word += one_character

    return Counter(vowels_in_word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_vowel_count)
