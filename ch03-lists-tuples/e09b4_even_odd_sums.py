#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 4: even_odd_sums"""


# Write a function that takes a list or tuple of numbers. Return a two-element list,
# containing (respectively) the sum of the even-indexed numbers and the sum of
# the odd-indexed numbers. So calling the function as even_odd_sums([10, 20,
# 30, 40, 50, 60]), you’ll get back [90, 120].


def even_odd_sums(any_type):
    return [sum(any_type[::2]),sum(any_type[1::2])]
