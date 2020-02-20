#!/usr/bin/env python3
"""Solution to chapter 5, exercise 18: get_final_line"""


def get_final_line(filename):
    """Given a filename, returns the final line in that file."""
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line
