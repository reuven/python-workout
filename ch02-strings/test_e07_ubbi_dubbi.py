from e07_ubbi_dubbi import ubbi_dubbi
from io import StringIO
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('papaya', 'pubapubayuba'),
    ('elephant', 'ubelubephubant'),
    ('testing', 'tubestubing'),
    ('banana', 'bubanubanuba'),
])
def test_simple(input_word, output_word):
    assert ubbi_dubbi(input_word) == output_word
