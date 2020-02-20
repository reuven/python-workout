import pytest
from e26_calc import calc


@pytest.mark.parametrize('to_solve, output', [
    ('+ 2 2', 4),
    ('- 2 3', -1),
    ('* 2 4', 8),
    ('/ 5 2', 2.5),
    ('** 2 6', 64),
    ('% 7 2', 1),
])
def test_simple(to_solve, output):
    assert calc(to_solve) == output
