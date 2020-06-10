#!/usr/bin/env python3

"""Solution to chapter 10, exercise 47: circle"""


class CircleIterator():
    """Iterator for Circle."""

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value


class Circle():
    """Class that produces an iterator, which repeatedly cycles
through the elements of an iterator until returning max_times
items. """

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)
