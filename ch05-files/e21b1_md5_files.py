#!/usr/bin/env python3
"""Solution to chapter 5, exercise 21, beyond 1: md5_files"""


import glob
import hashlib


def md5_files(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass

    return output
