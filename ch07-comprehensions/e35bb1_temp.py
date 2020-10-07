#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35b, beyond 1: temperature"""


def dict_f_to_c(dict_of_temps):
    return {key: (value-32)/1.8
            for key, value in dict_of_temps.items()}
