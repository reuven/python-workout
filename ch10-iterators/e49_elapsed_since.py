#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49: elapsed_since"""

import time


def elapsed_since(data):
    """A generator that takes an iterable as input.

With each iteration, it yields a tuple containing the
data and the time since the previous iteration.
"""
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)
