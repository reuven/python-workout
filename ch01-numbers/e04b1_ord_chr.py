#!/usr/bin/env python3
"""Solution to chapter 1, exercise 4, beyond 1: ord_hex"""


def ord_hex_output():
    """Get a hex number to convert. Use ord to turn it into an integer,
and print the decimal equivalent.
"""

    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    ord_0 = ord('0')
    ord_a_minus_10 = ord('a') - 10
    for power, digit in enumerate(reversed(hexnum)):
        if '0' <= digit <= '9':
            dec_digit = ord(digit) - ord_0
        elif 'a' <= digit.lower() <= 'z':
            dec_digit = ord(digit.lower()) - ord_a_minus_10

        decnum += dec_digit * (16 ** power)
    print(decnum)

ord_hex_output()
