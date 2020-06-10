from e47_circle import Circle
import pytest


@pytest.mark.parametrize('iterable, maxtimes, output', [
    ('abcd', 7, 'abcdabc'),
    ([10, 20, 30], 2, [10, 20]),
    ([10, 20, 30], 8, [10, 20, 30, 10, 20, 30, 10, 20]),
])
def test_circle(iterable, maxtimes, output):
    assert list(Circle(iterable, maxtimes)) == list(output)
