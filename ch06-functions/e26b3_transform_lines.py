#!/usr/bin/env python3

"""Solution to chapter 6, exercise 26, beyond 3: transform_lines"""


def transform_lines(f, infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f(one_line))
