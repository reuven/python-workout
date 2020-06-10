#!/usr/bin/env python3

"""Solution to chapter 10, exercise 46: myenumerate"""


class MyEnumerate():
    """Simple replacement for enumerate"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value
