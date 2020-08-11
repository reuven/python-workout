#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5, beyond 2: Pig Latin, handle punctuation"""


def pig_latin_punctuated(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string.

If the original word ends with punctuation, then
the output word ends with the same punctuation.
"""
    punctuation = ''
    if word[-1] in '.?!':
        punctuation = word[-1]
        word = word[:-1]

    if word[0].lower() in 'aeiou':
        output = f'{word}way'

    output = f'{word[1:]}{word[0]}ay'

    return output + punctuation
