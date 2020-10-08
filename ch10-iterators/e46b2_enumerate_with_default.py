#!/usr/bin/env python3

"""Solution to chapter 10, exercise 46, beyond 2: enumerate_with_default"""


class MyEnumerateIterator:
    def __init__(self, data, start):
        self.data = data
        self.index = start

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value


class MyEnumerate():
    """Simple replacement for enumerate"""

    def __init__(self, data, start=0):
        self.data = data
        self.start = start

    def __iter__(self):
        return MyEnumerateIterator(self.data, self.start)
