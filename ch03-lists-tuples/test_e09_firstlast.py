from e09_firstlast import firstlast
import pytest


@pytest.mark.parametrize('arg, output', [
    ('abcd', 'ad'),
    ([10, 20, 30, 40, 50], [10, 50]),
    ((10, 20, 30, 40), (10, 40)),
    ('ab', 'ab'),
    ('a', 'aa'),
    ([10], [10, 10])
])
def test_firstlast(arg, output):
    assert firstlast(arg) == output
