#!/usr/bin/env python3
"""Solution to chapter 5, exercise 20, beyond 2: file_sizes"""

import glob
import os


def file_sizes(dirname):
    counts = {one_filename: os.stat(one_filename).st_size
              for one_filename in glob.glob(f'{dirname}/*')
              if os.path.isfile(one_filename)}

    return counts
