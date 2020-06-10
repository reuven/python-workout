from e42_flexible_dict import FlexibleDict


def test_flexible_dict():
    fd = FlexibleDict()

    fd['a'] = 100
    assert fd['a'] == 100

    fd[5] = 500
    assert fd[5] == 500

    fd[1] = 100
    assert fd[1] == 100
    assert fd['1'] == 100

    fd['1'] = 100
    assert fd[1] == 100
    assert fd['1'] == 100
