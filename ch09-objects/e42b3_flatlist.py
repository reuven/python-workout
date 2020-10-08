#!/usr/bin/env python3

"""Solution to chapter 9, exercise 42, beyond 3: flat_list"""


class FlatList(list):
    def append(self, new_value):
        try:
            for one_item in new_value:
                list.append(self, one_item)
        except TypeError:
            list.append(self, new_value)
