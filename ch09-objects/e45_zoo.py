#!/usr/bin/env python3

"""Solution to chapter 9, exercise 45: zoo"""


class Zoo():
    """A class in which to place our animals."""

    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        """Add one or more cages to our zoo"""
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)

    def animals_by_color(self, color):
        """Return a list of Animal objects whose
color matches the requested color"""
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]

    def animals_by_legs(self, number_of_legs):
        """Return a list of Animal objects whose
number of legs matches the requested number"""
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        """Return the total number of legs of all animals"""
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)
