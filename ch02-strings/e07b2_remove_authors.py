#!/usr/bin/env python3
"""Solution to chapter 2, exercise 7, beyond 2: Remove authors' names"""

import string


def remove_authors_names(text, names):
    """Given a string (text) and a list of strings (names),
remove any occurence of a name from text and return it.
"""
    output = text

    for one_name in names:
        output = output.replace(one_name, '_' * len(one_name))

    return output
