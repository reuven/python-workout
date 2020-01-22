from e08_sort_string import strsort
from io import StringIO
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('abcdef', 'abcdef'),
    ('abcDEF', 'DEFabc'),
    ('ab c', ' abc'),
    ('abcdefabcdef', 'aabbccddeeff')
])
def test_strsort(input_word, output_word):
    assert strsort(input_word) == output_word
