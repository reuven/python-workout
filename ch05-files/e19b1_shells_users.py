#!/usr/bin/env python3
"""Solution to chapter 5, exercise 19, beyond 1: shells_users"""

from collections import defaultdict


def shells_users(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, *ignore, shell = one_line.strip().split(':')

        output[shell].append(username)

    return output
