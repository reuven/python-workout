from e10_sum_anything import mysum
import pytest


@pytest.mark.parametrize('args, output', [
    ((), ()),
    ((10, 20, 30), 60),
    (('a', 'b', 'c'), 'abc'),
    ([10, 20, 30], 60)
])
def test_mysum(args, output):
    assert mysum(*args) == output
