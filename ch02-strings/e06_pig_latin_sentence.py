#!/usr/bin/env python3
"""Solution to chapter 2, exercise 6: pl_sentence"""


def pl_sentence(sentence):
    """Get a sentence from the user, containing
lowercase, unpuncutated words. Return the
sentence, translated into Pig Latin.
"""
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)
