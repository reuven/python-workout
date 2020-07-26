#!/usr/bin/env python3
"""Solution to chapter 1, exercise 3, beyond 1: before_after_dot"""


def before_after_dot(f, before, after):
    """Accepts a float, and two integers.

Returns a float containing before digits preceding the dcimal point,
and after digits following the decimal point.
"""
    s = str(f)
    i = s.index('.')
    return s[i-before:i+after+1]
