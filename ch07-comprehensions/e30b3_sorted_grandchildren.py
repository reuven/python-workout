#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 3: sorted_grandchildren"""


import operator


def sorted_grandchildren(d):
    grandchildren = [one_grandchild
                     for one_grandchild_list in d.values()
                     for one_grandchild in one_grandchild_list]

    return [one_grandchild['name']
            for one_grandchild in sorted(grandchildren,
                                         key=operator.itemgetter('age'))]
