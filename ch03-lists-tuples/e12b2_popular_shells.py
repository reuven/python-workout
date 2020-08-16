#!/usr/bin/env python3
"""Solution to chapter 3, exercise 12, beyond 2: shells_by_popularity"""

from collections import Counter
import operator


def shells_by_popularity(filename):
    shells = Counter(one_line.split(':')[-1].strip()
                     for one_line in open(filename)
                     if not one_line.startswith(('#', '\n')))

    return sorted(shells.items(),
                  key=operator.itemgetter(1), reverse=True)
