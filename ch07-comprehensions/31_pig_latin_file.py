#!/usr/bin/env python3


def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'


def plfile(filename):
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())
