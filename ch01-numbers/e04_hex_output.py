#!/usr/bin/env python3
"""Solution to chapter 1, exercise 4: hex_output"""


def hex_output():
    """Ask the user to enter a valid hexadecimal number, and print the decimal equivalent."""

    d = 0
    h = input("Enter a hex number to convert to decimal: ")
    for power, digit in enumerate(reversed(h)):
        d += int(digit, 16) * (16 ** power)
    print(d)
