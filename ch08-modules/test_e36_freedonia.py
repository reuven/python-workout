from e36_freedonia import time_percentage, calculate_tax
import pytest
from math import isclose


@pytest.mark.parametrize('hour,percentage', [
    (0, 0),
    (12, 0.5),
    (18, 0.75),
    (23, 0.958)
])
def test_time_percentage(hour, percentage):
    assert isclose(time_percentage(hour), percentage, rel_tol=0.05)


@pytest.mark.parametrize('amount,state,hour,tax', [
    (500, 'Harpo', 12, 625),
    (500, 'Harpo', 21, 718),
])
def test_calculate_tax(amount, state, hour, tax):
    assert isclose(calculate_tax(amount, state, hour), tax, rel_tol=0.05)
