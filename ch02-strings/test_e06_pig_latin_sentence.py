from e06_pig_latin_sentence import pl_sentence
from io import StringIO
import pytest


@pytest.mark.parametrize('input_words, output_words', [
    ('papaya', 'apayapay'),
    ('elephant', 'elephantway'),
    ('this is a test', 'histay isway away esttay'),
    ('python is the best language ever', 'ythonpay isway hetay estbay anguagelay everway')])
def test_simple(input_words, output_words):
    assert pl_sentence(input_words) == output_words
