#!/usr/bin/env python3


def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys() < 1 >

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)] < 2 >
    return output
