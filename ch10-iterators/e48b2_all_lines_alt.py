#!/usr/bin/env python3

"""Solution to chapter 10, exercise 48, beyond 2: all_lines_alt"""

import os


def open_file_safely(filename):
    try:
        return open(filename)
    except OSError:
        return None


def all_lines_alt(path):
    all_files = [open_file_safely(os.path.join(path, filename))
                 for filename in os.listdir(path)]

    while all_files:
        for one_file in all_files:
            if one_file is None:
                all_files.remove(one_file)
                continue

            one_line = one_file.readline()

            if one_line:
                yield one_line
            else:
                all_files.remove(one_file)
