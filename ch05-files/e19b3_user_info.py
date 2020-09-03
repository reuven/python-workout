#!/usr/bin/env python3
"""Solution to chapter 5, exercise 19, beyond 2: user_info"""


def user_info(filename):
    output = {}

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, passwd, uid, *ignore, homedir, shell = one_line.strip().split(':')

        output[username] = {'uid': uid,
                            'homedir': homedir,
                            'shell': shell}

    return output
