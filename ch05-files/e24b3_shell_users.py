#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24, beyond 3: shell_users"""

from collections import defaultdict


def shell_users(filename, outfilename):
    shells = defaultdict(list)

    with open(filename) as passwd, open(outfilename, 'w') as outfile:
        for one_line in passwd:
            if one_line.startswith(('#', '\n')):
                continue

            username, *fields, shell = one_line.strip().split(':')
            shells[shell].append(username)

        for shell, all_users in shells.items():
            outfile.write(f'{shell}\t{",".join(all_users)}\n')
