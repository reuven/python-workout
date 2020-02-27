from e32_flipped_dict import flipped_dict
import pytest


@pytest.mark.parametrize('d, fd', [
    ({}, {}),
    ({'a': 1}, {1: 'a'}),
    ({'a': 1, 'b': 2, 'c': 3}, {1: 'a', 2: 'b', 3: 'c'}),
    ({'a': 1, 'a': 2, 'a': 3}, {3: 'a'})
])
def test_flipped_dict(d, fd):
    assert flipped_dict(d) == fd
