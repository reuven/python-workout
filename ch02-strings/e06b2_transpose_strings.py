#!/usr/bin/env python3
"""Solution to chapter 2, exercise 6, beyond 2: Transpose strings"""


def transpose_strings(list_of_words):
    """Given a list of strings, each of which contains
multiple words, transpose them.  So  given input of

    ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

the output would be

    ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].

We assume that each of the strings contains
the same number of words.

"""

    return [' '.join(t)
            for t in (zip(*[s.split()
                            for s in list_of_words]))]
