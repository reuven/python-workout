from e46_myenumerate import MyEnumerate


def test_simple():
    m = MyEnumerate('abc')
    assert list(m) == [(0, 'a'), (1, 'b'), (2, 'c')]


def test_is_iterable():
    m = MyEnumerate('abc')
    assert hasattr(m, '__iter__')
