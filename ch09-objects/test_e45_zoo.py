from e43_animals import Animal, Wolf, Sheep, Snake, Parrot
from e44_cages import Cage
from e45_zoo import Zoo


def test_zoo():

    wolf = Wolf('black')
    sheep1 = Sheep('black')
    sheep2 = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    c1 = Cage(1)
    c2 = Cage(2)

    c1.add_animals(wolf, sheep1, sheep2)
    c2.add_animals(snake, parrot)

    z = Zoo()
    z.add_cages(c1, c2)
    assert len(z.cages) == 2
    assert z.animals_by_color('black') == [wolf, sheep1]
    assert z.animals_by_legs(4) == [wolf, sheep1, sheep2]
    assert z.number_of_legs() == 14

    assert str(z) == """Cage 1
\tblack Wolf, 4 legs
\tblack Sheep, 4 legs
\twhite Sheep, 4 legs
Cage 2
\tbrown Snake, 0 legs
\tgreen Parrot, 2 legs"""
