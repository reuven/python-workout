#!/usr/bin/env python3


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
for scoop in scoops:
    print(scoop.flavor)
