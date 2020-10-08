#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38, beyond 2: beverage_default_temp"""


class Beverage:
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp
