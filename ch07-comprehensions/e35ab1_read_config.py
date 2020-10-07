#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35a, beyond 1: read_config"""

# Yes, this is a duplicate of e32 b3!  Sorry!


def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}
