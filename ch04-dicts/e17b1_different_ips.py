#!/usr/bin/env python3
"""Solution to chapter 4, exercise 17, beyond 1: different_ips"""


def different_ips(filename):
    return {one_line.split()[0]
            for one_line in open(filename)}
