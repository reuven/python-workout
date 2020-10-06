#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23, beyond 2: json_passwd_dict"""


import json


def json_passwd_dict(filename):
    fields = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']

    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(dict(zip(fields, one_line.split(':'))))

    return json.dumps(output)
