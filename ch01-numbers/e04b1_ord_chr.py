#!/usr/bin/env python3
"""Solution to chapter 1, exercise 4, beyond 1: ord_hex"""


def ord_hex_output():
    """Get a hex number to convert. Use ord to turn it into an integer,
and print the decimal equivalent.
"""

    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87

        decnum += dec_digit * (16 ** power)
    print(decnum)
