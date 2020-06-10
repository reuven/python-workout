#!/usr/bin/env python3

"""Solution to chapter 9, exercise 42: flexible dict"""


class FlexibleDict(dict):
    """Dict that lets you use a string or int somewhat interchangeably."""

    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)
