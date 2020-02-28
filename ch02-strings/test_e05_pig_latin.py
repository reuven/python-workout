from e05_pig_latin import pig_latin
from io import StringIO
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('computer', 'omputercay'),
    ('table', 'abletay'),
    ('papaya', 'apayapay'),
    ('elephant', 'elephantway'),
    ('octopus', 'octopusway'),
    ('insightful', 'insightfulway')])
def test_simple(input_word, output_word):
    assert pig_latin(input_word) == output_word
