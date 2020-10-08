#!/usr/bin/env python3

"""Solution to chapter 9, exercise 42, beyond 1: string_key_dict"""


class StringKeyDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)
