#!/usr/bin/env python3

"""Solution to chapter 9, exercise 40, beyond 1: population"""


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
