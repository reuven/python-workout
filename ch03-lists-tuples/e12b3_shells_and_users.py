#!/usr/bin/env python3
"""Solution to chapter 3, exercise 12, beyond 3: shells_and_users"""

from collections import defaultdict


def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue

        username, *rest, shell = one_line.strip().split(':')

        shells[shell].append(username)

    return sorted(shells.items(), key=len)
