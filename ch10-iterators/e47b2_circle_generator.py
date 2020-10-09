#!/usr/bin/env python3

"""Solution to chapter 10, exercise 47, beyond 2: circle_generator"""


def circle(data, max_times):

    for index in range(max_times):
        yield data[index % len(data)]
