#!/usr/bin/env python3

"""Solution to chapter 9, exercise 43, beyond 1: legged_animals"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class TwoLeggedAnimal(Animal):
    number_of_legs = 2

class FourLeggedAnimal(Animal):
    number_of_legs = 4

class ZeroLeggedAnimal(Animal):
    number_of_legs = 0

class Wolf(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""

class Sheep(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""

class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""

class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""
