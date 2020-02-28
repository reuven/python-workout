#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5: pig_latin"""


def pig_latin():
    """Ask the user for a lowercase, unpunctuated word,
and print the translation into Pig Latin.
"""
    word = input("Enter a word: ")

    if word[0] in 'aeiou':
        print(f'{word}way')
    else:
        print(f'{word[1:]}{word[0]}ay')
