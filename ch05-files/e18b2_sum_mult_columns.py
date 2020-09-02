#!/usr/bin/env python3
"""Solution to chapter 5, exercise 18, beyond 2: sum_mult_columns"""


def sum_mult_columns(filename):
    total = 0

    for one_line in open(filename):
        fields = one_line.split()

        if len(fields) != 2:
            continue

        first, second = fields

        if not first.isdigit():
            continue

        if not second.isdigit():
            continue

        total += int(first) * int(second)

    return total
