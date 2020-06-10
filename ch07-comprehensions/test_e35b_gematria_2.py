from e35b_gematria_2 import gematria_equal_words, gematria_for
import pytest


@pytest.mark.parametrize('word, result', [
    ('abc', 6),
    ('abcd', 10)
])
def test_gematria_for(word, result):
    assert gematria_for(word) == result


def test_gematria_equal_words():
    output = gematria_equal_words('taxi')
    assert len(output) == 1032
    assert 'search' in output
    assert 'pooh' in output
    assert 'zoid' in output
