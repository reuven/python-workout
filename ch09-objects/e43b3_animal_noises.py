#!/usr/bin/env python3

"""Solution to chapter 9, exercise 43, beyond 3: animal_noises"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.sound}--{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    """Class for creating 4-legged wolves of any color"""

    sound = 'awooo'

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    """Class for creating 4-legged sheep of any color"""

    sound = 'baa'

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    """Class for creating 0-legged snakes of any color"""

    sound = 'hiss'

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    """Class for creating 2-legged parrots of any color"""

    sound = 'Polly wants a cracker!'

    def __init__(self, color):
        super().__init__(color, 2)
