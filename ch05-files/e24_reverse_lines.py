#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24: reverse_lines"""


def reverse_lines(infilename, outfilename):
    """Takes two filenames as arguments. The
first is for reading, and the second is for writing.
The contents of the first file are written to
the second, but in reverse order.
"""
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')
