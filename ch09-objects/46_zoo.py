#!/usr/bin/env python3


class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)

    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]

    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)


z = Zoo()
z.add_cages(c1, c2)
print(z)
