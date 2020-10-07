#!/usr/bin/env python3

"""Solution to chapter 7, exercise 33, beyond 2: file_info"""

# Yes, this is a duplicate of exercise 33, beyond 2!  Whoops...

import glob
import os


def file_info(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}
