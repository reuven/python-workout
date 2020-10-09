#!/usr/bin/env python3

"""Solution to chapter 10, exercise 47, beyond 3: myrange"""


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.current = 0
            self.stop = first
        else:
            self.current = first
            self.stop = second
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value
