from e43_animals import Animal, Wolf, Sheep, Snake, Parrot
from e44_cages import Cage
import pytest


def test_cage_creation():
    c = Cage(1)
    assert c.id_number == 1
    assert c.animals == []


def test_add_animals_to_cages():
    c = Cage(1)
    wolf = Wolf('black')
    sheep1 = Sheep('black')
    sheep2 = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    c.add_animals(wolf, sheep1, sheep2)
    assert len(c.animals) == 3
    c.add_animals(snake, parrot)
    assert len(c.animals) == 5

    assert str(c) == """Cage 1
\tblack Wolf, 4 legs
\tblack Sheep, 4 legs
\twhite Sheep, 4 legs
\tbrown Snake, 0 legs
\tgreen Parrot, 2 legs"""
