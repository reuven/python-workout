#!/usr/bin/env python3


class Animal():
    def __init__(self, color, number_of_legs):
    self.species = self.__class__.__name__
    self.color = color
    self.number_of_legs = number_of_legs

    def __repr__(self):
        return f"{self.color} {self.species}, {self.number_of_legs} legs"


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

print(wolf)
print(sheep)
print(snake)
print(parrot)
