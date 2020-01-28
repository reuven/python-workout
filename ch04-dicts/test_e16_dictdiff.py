from e16_dictdiff import dictdiff
import pytest


@pytest.fixture
def simple_dict1():
    return {'a': 1, 'b': 2, 'c': 3}


@pytest.fixture
def simple_dict2():
    return {'a': 1, 'b': 2, 'c': 4}


@pytest.fixture
def simple_dict3():
    return {'a': 1, 'b': 2, 'd': 3}


def test_empty():
    assert dictdiff({}, {}) == {}


def test_same(simple_dict1):
    assert dictdiff(simple_dict1, simple_dict1) == {}


def test_simple_diff1(simple_dict1, simple_dict2):
    assert dictdiff(simple_dict1, simple_dict2) == {'c': [3, 4]}


def test_simple_diff2(simple_dict1, simple_dict3):
    assert dictdiff(simple_dict1, simple_dict3) == {
        'c': [3, None], 'd': [None, 3]}


def test_simple_diff_bw(simple_dict1, simple_dict3):
    assert dictdiff(simple_dict3, simple_dict1) == {
        'c': [None, 3], 'd': [3, None]}
