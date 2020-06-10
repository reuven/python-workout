#!/usr/bin/env python3

"""Solution to chapter 9, exercise 44: cages"""


class Cage():
    """Class for creating cages in which to put cute, furry animals."""

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        """Add one or more animals to a cage.  Returns None."""
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output
