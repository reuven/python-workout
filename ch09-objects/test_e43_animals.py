from e43_animals import Animal, Wolf, Sheep, Snake, Parrot
import pytest


@pytest.mark.parametrize('species, color, output', [
    (Wolf, 'black', 'black Wolf, 4 legs'),
    (Sheep, 'white', 'white Sheep, 4 legs'),
    (Snake, 'brown', 'brown Snake, 0 legs'),
    (Parrot, 'green', 'green Parrot, 2 legs')
])
def test_animal(species, color, output):
    a = species(color)
    assert str(a) == output
