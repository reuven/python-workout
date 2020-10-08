#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38, beyond 3: logfile"""


class Logfile:
    def __init__(self, filename):
        self.file = open(filename, 'w')
