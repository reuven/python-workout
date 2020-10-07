#!/usr/bin/env python3

"""Solution to chapter 7, exercise 28, beyond 1: join_under_10"""


def join_under_10(numbers):
    return ','.join(str(number)
                    for number in numbers
                    if 0 <= number <= 10)
