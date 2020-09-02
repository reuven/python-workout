#!/usr/bin/env python3
"""Solution to chapter 5, exercise 18, beyond 3: count_vowels"""


def count_vowels(filename):
    output = dict.fromkeys('aeiou', 0)

    for one_line in open(filename):
        for one_character in one_line.lower():
            if one_character in output:
                output[one_character] += 1

    return output
