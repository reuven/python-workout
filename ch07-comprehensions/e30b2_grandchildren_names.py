#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 2: grandchildren_names"""


def grandchildren_names(d):
    return [one_grandchild
            for grandchild_list in d.values()
            for one_grandchild in grandchild_list]
