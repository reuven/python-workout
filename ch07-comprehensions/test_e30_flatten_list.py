from e30_flatten_list import flatten
import pytest


@pytest.mark.parametrize('nested, output', [
    ([[10, 20, 30]], [10, 20, 30]),
    ([[10, 20], [30, 40]], [10, 20, 30, 40]),
])
def test_flatten(nested, output):
    assert flatten(nested) == output
