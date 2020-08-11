#!/usr/bin/env python3
"""Solution to chapter 2, exercise 7, beyond 3: URL-encoding"""

import string


def url_encode(text):
    """Given a string, replace any character that
isn't a letter or number with % and its two-digit
hex code.
"""
    safe_chars = string.ascii_letters + string.digits
    output = []

    for one_character in text:
        if one_character in safe_chars:
            output.append(one_character)
        else:
            output.append(hex(ord(one_character)).replace('0x', '%'))

    return ''.join(output)
