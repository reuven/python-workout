#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 1: flatten_odd_ints"""


def flatten_odd_ints(mylist):
    return [int(str(one_element))
            for one_sublist in mylist
            for one_element in one_sublist
            if str(one_element).strip().isdigit() and int(one_element) % 2 == 1]
