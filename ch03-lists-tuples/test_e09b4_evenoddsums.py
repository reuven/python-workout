from e09b4_even_odd_sums import even_odd_sums
import pytest


@pytest.mark.parametrize('arg, output', [
    ([10, 20, 30,40,50,60], [90, 120]),
    ([10, 20, 30, 40, 50], [90, 60]),
    ((10, -20, -30, 40), (-20, 20)),
    ([10], [10])
])
def test_evenoddsums(arg, output):
    assert even_odd_sums(arg) == output
