#!/usr/bin/env python3


infilename = 'input.txt'
outfilename = 'output.txt'

with open(infilename) as infile, open(outfilename, 'w') as outfile:
    for one_line in infile:
        outfile.write(f"{one_line.rstrip()[::-1]}\n")
