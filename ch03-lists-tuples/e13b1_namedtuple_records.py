#!/usr/bin/env python3
"""Solution to chapter 3, exercise 13, beyond 1: namedtuple_records"""


import operator
from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'distance'])


PEOPLE = [Person('Donald', 'Trump', 7.85),
          Person('Vladimir', 'Putin', 3.626),
          Person('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output
