#!/usr/bin/env python3

"""Solution to chapter 10, exercise 47, beyond 1: circle_inherit"""


class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        iterated_data = getattr(self, self.returns)

        value = iterated_data[self.index % len(iterated_data)]
        self.index += 1
        return value

    def __iter__(self):
        return type(self)(self.data, self.max_times)


class Circle(CircleIterator):
    def __init__(self, data, max_times):
        super().__init__(data, max_times)
        self.returns = 'data'
