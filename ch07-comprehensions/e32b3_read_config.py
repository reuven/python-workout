#!/usr/bin/env python3

"""Solution to chapter 7, exercise 32, beyond 3: read_config"""


def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}
