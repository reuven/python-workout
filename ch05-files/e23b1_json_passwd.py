#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23, beyond 1: json_passwd"""


import json


def json_passwd(filename):
    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(tuple(one_line.split(':')))

    return json.dumps(output)
