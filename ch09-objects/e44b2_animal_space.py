#!/usr/bin/env python3

"""Solution to chapter 9, exercise 44, beyond 2: animal_space"""


class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    space_required = 10

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    space_required = 5

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    space_required = 2

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    space_required = 1

    def __init__(self, color):
        super().__init__(color, 2)


class NotEnoughSpaceError(Exception):
    pass


class Cage():

    def __init__(self, id_number, total_space):
        self.id_number = id_number
        self.animals = []
        self.total_space = total_space

    def add_animals(self, *animals):
        for one_animal in animals:
            if self.space_used() + one_animal.space_required > self.total_space:
                raise NotEnoughSpaceError(
                    f'Not enough room for your {one_animal}')

            self.animals.append(one_animal)

    def space_used(self):
        return sum(one_animal.space_required
                   for one_animal in self.animals)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


class BigCage(Cage):
    max_animals = 5
