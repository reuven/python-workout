#!/usr/bin/env python3


class CircleIterator():
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

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)


c = Circle('abc', 5)
print(list(c))        # prints a, b, c, a, b
