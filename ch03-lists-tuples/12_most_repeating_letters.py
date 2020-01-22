#!/usr/bin/env python3

from collections import Counter
import operator

words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word): < 1 >


return Counter(word).most_common(1)[0][1] < 2 >


def most_repeating_word(words):
    word_counts = {word: most_repeating_letter_count(word)
                   for word in words}

    return max(word_counts.items(), key=operator.itemgetter(1))[0] < 3 >


most_repeating_word(words)
