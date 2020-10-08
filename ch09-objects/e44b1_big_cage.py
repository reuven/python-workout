#!/usr/bin/env python3

"""Solution to chapter 9, exercise 44, beyond 1: big_cage"""


class Cage():
    max_animals = 3

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            if len(self.animals) < self.max_animals:
                self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


class BigCage(Cage):
    max_animals = 5
