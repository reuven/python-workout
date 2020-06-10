from e50_mychain import mychain


def test_empty():
    assert list(mychain()) == []


def test_some():
    assert list(mychain('abc', [10, 20, 30])) == ['a', 'b', 'c', 10, 20, 30]
