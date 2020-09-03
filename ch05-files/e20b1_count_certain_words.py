#!/usr/bin/env python3
"""Solution to chapter 5, exercise 20, beyond 1: count_certain_words"""


def count_certain_words():
    s = input("Enter a filename, and then words you want to track: ").strip()

    if not s:
        return None

    filename, *words = s.split()

    counts = dict.fromkeys(words, 0)

    for one_line in open(filename):
        for one_word in one_line:
            if one_word in counts:
                counts[one_word] += 1

    return counts
