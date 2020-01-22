#!/usr/bin/env python3


class Cage():

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
    output = f"Cage {self.id_number}\n"
    output += '\n'.join('\t' + str(animal)
                        for animal in self.animals)
    return output


c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
