#!/usr/bin/env python3


def flatten(mylist):
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]


print(flatten([[1, 2], [3, 4]]))    # [1,2,3,4]
