#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35a, beyond 2: read_config_int"""


def read_config(filename):
    return {one_line.split('=')[0]: int(one_line.split('=')[1].strip())
            for one_line in open(filename)
            if one_line.split('=')[1].strip().isdigit()}
