#!/usr/bin/env python3
"""Solution to chapter 6, exercise 25, beyond 1: copyfile"""


def copyfile(infilename, *args):
    for outfilename in args:
        with open(outfilename, 'w') as outfile:
            for one_line in open(infilename):
                outfile.write(one_line)
