#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49, beyond 1: elapsed_since_wait"""

import time


def elapsed_since(data, min_wait):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < min_wait:
            time.sleep(min_wait - delta)

        last_time = time.perf_counter()
        yield (delta, item)
