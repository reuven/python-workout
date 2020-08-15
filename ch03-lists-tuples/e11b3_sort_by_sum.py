#!/usr/bin/env python3
"""Solution to chapter 3, exercise 11, beyond 3: sort_by_vowel_sum"""


def sort_by_sum(list_of_lists):
    """Given a list of lists, in which the inner lists contain
numbers, return the outer list sorted by each inner list's sum.
"""
    return sorted(list_of_lists, key=sum)
