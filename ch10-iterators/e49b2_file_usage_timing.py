#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49, beyond 2: file_usage_timing"""

import os


def file_usage_timing(dirname):
    for one_filename in os.listdir(dirname):
        full_filename = os.path.join(dirname, one_filename)

        yield (full_filename,
               os.stat(full_filename).st_mtime,
               os.stat(full_filename).st_ctime,
               os.stat(full_filename).st_atime)
