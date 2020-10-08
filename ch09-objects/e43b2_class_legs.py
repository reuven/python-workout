#!/usr/bin/env python3

"""Solution to chapter 9, exercise 43, beyond 2: class_legs"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    """Class for creating 4-legged wolves of any color"""

    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)


class Sheep(Animal):
    """Class for creating 4-legged sheep of any color"""

    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)


class Snake(Animal):
    """Class for creating 0-legged snakes of any color"""

    number_of_legs = 0

    def __init__(self, color):
        super().__init__(color)


class Parrot(Animal):
    """Class for creating 2-legged parrots of any color"""

    number_of_legs = 2

    def __init__(self, color):
        super().__init__(color)
