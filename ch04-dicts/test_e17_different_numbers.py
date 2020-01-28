from e17_different_numbers import how_many_different_numbers
import pytest


def test_empty():
    assert how_many_different_numbers([]) == 0


def test_all_different():
    assert how_many_different_numbers([10, 20, 30]) == 3


def test_all_same():
    assert how_many_different_numbers([10, 10, 10]) == 1


def test_same_even_if_float():
    assert how_many_different_numbers([10, 10.0, 10]) == 1
