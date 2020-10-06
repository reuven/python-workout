#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23, beyond 3: file_info"""


import os
import glob
import json


def write_file_info(dirname, outputfile):
    output = []
    for one_filename in glob.glob(f'{dirname}/*'):
        if not os.path.isfile(one_filename):
            continue

        try:
            output.append({'filename': one_filename,
                           'size': os.stat(one_filename).st_size,
                           'mtime': os.stat(one_filename).st_mtime})
        except:
            print(f'Error reading {filename}; skipping')

    return json.dump(output, open(outputfile, 'w'))


def read_file_info(filename):
    output = {}

    file_info = json.load(filename)

    return output
