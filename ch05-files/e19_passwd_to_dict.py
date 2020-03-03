#!/usr/bin/env python3
"""Solution to chapter 5, exercise 19: passwd_to_dict"""


def passwd_to_dict(filename):
    """Expects to get a string argument, the name of a file in passwd format.
Returns a dictionary in which the keys are the usernames from the file,
and the values are the user IDs from the file.  The user IDs should be
returned as integers.
"""
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users
