#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 3: words summary"""


def summarize(words):
    """Accepts a list of strings.

Returns a 3-element tuple containing three integers: (a) length
of the shortest word, (b) length of the longest word, and (c)
average word length.
"""
    word_lengths = [len(one_word)
                    for one_word in words]

    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)
