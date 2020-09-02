#!/usr/bin/env python3
"""Solution to chapter 4, exercise 17, beyond 3: different_extensions"""

import os


def different_extensions(dirname):
    return {os.path.splitext(one_filename)[-1]
            for one_filename in os.listdir(dirname)}
