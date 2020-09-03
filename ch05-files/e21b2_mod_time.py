#!/usr/bin/env python3
"""Solution to chapter 5, exercise 21, beyond 2: mod_times"""


import glob
import os


def mod_times(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            mod_time = os.stat(one_filename).ST_MTIME
            output[one_filename] = (arrow.now() - arrow.get(1503636889)).days

        except:
            pass

    return output
