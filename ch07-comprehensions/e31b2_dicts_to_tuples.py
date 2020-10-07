#!/usr/bin/env python3

"""Solution to chapter 7, exercise 31, beyond 2: dicts_to_tuples"""


def dicts_to_tuples(list_of_dicts):
    return [one_tuple
            for one_dict in list_of_dicts
            for one_tuple in one_dict.items()]
