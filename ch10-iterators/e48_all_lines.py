#!/usr/bin/env python3

"""Solution to chapter 10, exercise 48: all_lines"""


import os


def all_lines(path):
    """An iterator that returns, one at a time, each line
from each file in a named directory.

Any file that cannot be opened, for whatever reason, is ignored.
"""
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass
