#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35b: gematria_equal_words"""

from e35a_gematria_1 import gematria_dict

GEMATRIA = gematria_dict()


def gematria_for(word):
    """Function that calculates the gematria
for a given word, an argument passed as a string.
"""
    return sum(GEMATRIA.get(one_char, 0)
               for one_char in word)


def gematria_equal_words(input_word):
    """Function that takes a string (word) as input,
and returns a list of strings (words) whose calculated
gematria is identical.
"""
    our_score = gematria_for(input_word.lower())
    return [one_word.strip()
            for one_word in open('/usr/share/dict/words')
            if gematria_for(one_word.lower()) == our_score]
