#!/usr/bin/env python3

"""Solution to chapter 6, exercise 26, beyond 1: calc_args"""

import operator


def calc_args(to_solve):

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, *numbers = to_solve.split()

    if not numbers:
        return 0

    output = int(numbers[0])
    for one_number in numbers[1:]:
        output = operations[op](output, int(one_number))

    return output
