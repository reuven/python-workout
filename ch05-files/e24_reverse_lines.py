#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24: reverse_lines"""


infilename = 'input.txt'
outfilename = 'output.txt'

with open(infilename) as infile, open(outfilename, 'w') as outfile:
    for one_line in infile:
        outfile.write(f'{one_line.rstrip()[::-1]}\n')
