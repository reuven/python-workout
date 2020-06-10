#!/usr/bin/env python3

"""Solution to chapter 6, exercise 26: calc"""

import operator


def calc(to_solve):
    """This function expects to get a string containing a
two-argument math expression in prefix notation, and with
whitespace separating the operator and numbers.
The return value is the result from invoking this operation.
"""

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)
