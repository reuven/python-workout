#!/usr/bin/env python3
"""Solution to chapter 6, exercise 25, beyond 3: anyjoin"""


def anyjoin(seq, glue=' '):
    return glue.join([str(one_item)
                      for one_item in seq])
