#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9: firstlast"""


def firstlast(sequence):
    """Given a sequence, returns a two-element sequence.
The returned sequence will be of the same type as the argument.
Its two elements will be the argument's first and last elements.
"""
    return sequence[:1] + sequence[-1:]
