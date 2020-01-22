#!/usr/bin/env python3


def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output
