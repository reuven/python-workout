from e33_transform_values import transform_values
import pytest


@pytest.mark.parametrize('f,d,output', [
    (abs, {'a': 1, 'b': -2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}),
    (len, {'first': 'Reuven', 'last': 'Lerner'},
     {'first': 6, 'last': 6})
])
def test_transform_values(f, d, output):
    assert transform_values(f, d) == output
