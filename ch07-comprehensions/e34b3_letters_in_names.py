#!/usr/bin/env python3

"""Solution to chapter 7, exercise 34, beyond 3: letters_in_names"""


import string


def letters_in_names(list_of_names):
    return {one_letter
            for one_letter in ''.join(list_of_names)
            if one_letter in string.ascii_letters}
