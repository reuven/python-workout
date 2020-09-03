#!/usr/bin/env python3
"""Solution to chapter 5, exercise 20, beyond 3: most_common_letters"""

from collections import Counter
import glob


def most_common_letters(dirname):
    counts = Counter()

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            for one_line in open(one_filename):
                counts.update(one_line)
        except:
            pass

    return list(dict(counts.most_common(5)).keys())
