#!/usr/bin/env python3

"""Solution to chapter 10, exercise 48, beyond 3: all_lines_matching"""

import os


def all_lines(path, s):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                if s in line:
                    yield line
        except OSError:
            pass
