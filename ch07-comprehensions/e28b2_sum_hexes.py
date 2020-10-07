#!/usr/bin/env python3

"""Solution to chapter 7, exercise 28, beyond 2: sum_hexes"""


def sum_hexes(hex_numbers):
    return sum(int(one_number, 16)
               for one_number in hex_numbers)
