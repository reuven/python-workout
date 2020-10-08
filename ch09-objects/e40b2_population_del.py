#!/usr/bin/env python3

"""Solution to chapter 9, exercise 40, beyond 2: population_del"""


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1
