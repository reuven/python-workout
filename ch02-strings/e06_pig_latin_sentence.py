#!/usr/bin/env python3
"""Solution to chapter 2, exercise 6: pl_sentence"""


def pl_sentence():
    """Ask the user to enter lowercase, unpuncutated words.
Print the sentence, translated into Pig Latin.
"""
    sentence = input("Enter a sentence: ")

    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f"{word}way")
        else:
            output.append(f"{word[1:]}{word[0]}ay")

    print(' '.join(output))
