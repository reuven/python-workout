#!/usr/bin/env python3

"""Solution to chapter 7, exercise 31, beyond 3: most_popular_hobbies"""


import collections


def most_popular_hobbies(list_of_dicts):
    return collections.Counter([one_hobby
                                for one_person in list_of_dicts
                                for one_hobby in one_person['hobbies']]).most_common(3)
