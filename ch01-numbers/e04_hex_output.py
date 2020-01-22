#!/usr/bin/env python3
"""Ask the user for a hex number, and convert it to decimal"""


def hex_output():
    """Ask the user to enter a valid hexadecimal number, and print the decimal equivalent."""

    d = 0
    h = input("Enter a hex number to convert to decimal: ")
    for power, digit in enumerate(reversed(h)):
        d += int(digit, 16) * (16 ** power)
    print(d)
