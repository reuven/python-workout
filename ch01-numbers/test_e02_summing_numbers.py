import pytest
from e02_summing_numbers import mysum


@pytest.mark.parametrize('inputs, expected_sum', [
    ((), 0),
    ((10,), 10),
    ((10, 20, 30), 60),
    ((10.5, 20, 30), 60.5)
])
def test_mysum(inputs, expected_sum):
    assert mysum(*inputs) == expected_sum
