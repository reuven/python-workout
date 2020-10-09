#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 4: sum intable"""


def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False


def sum_intable(items):
    """Accepts a list of Python objects.

Sums those objects that are integers or can be
turned into integers.
"""

    return sum(one_item
               for one_item in items
               if is_intable(one_item))
