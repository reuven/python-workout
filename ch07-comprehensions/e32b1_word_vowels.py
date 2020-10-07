#!/usr/bin/env python3

"""Solution to chapter 7, exercise 32, beyond 1: word_vowels"""


def vowel_count(word):
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total += 1
    return total


def word_vowels(s):
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}
