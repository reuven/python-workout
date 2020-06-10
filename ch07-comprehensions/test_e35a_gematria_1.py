from e35a_gematria_1 import gematria_dict


def test_gematria_dict():
    d = gematria_dict()
    assert type(d) == dict
    assert len(d) == 26
    assert d['a'] == 1
    assert d['e'] == 5
    assert d['y'] == 25
