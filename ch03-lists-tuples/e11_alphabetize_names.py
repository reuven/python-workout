#!/usr/bin/env python3
"""Solution to chapter 3, exercise 11: alphabetize_names"""

import operator


PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]


def alphabetize_names(list_of_dicts):
    """Take a list of dicts describing people,
each with first/last/email as keys.

Return a new list of dicts,
sorted first by last name and then by first name.

If passed an empty list, then return an empty list.
"""
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))
