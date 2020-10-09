#!/usr/bin/env python3

"""Solution to chapter 10, exercise 48, beyond 1: all_lines_tuple"""

import os


def all_lines_tuple(path):
    for file_index, filename in enumerate(os.listdir(path)):
        full_filename = os.path.join(path, filename)
        try:
            for line_index, line in enumerate(open(full_filename)):

                yield (full_filename, file_index, line_index, line)
        except OSError:
            pass
