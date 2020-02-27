from e31_pig_latin_file import plword, plfile
import pytest


@pytest.mark.parametrize('word, pword', [
    ('test', 'esttay'),
    ('octopus', 'octopusway'),
    ('papaya', 'apayapay')
])
def test_plword(word, pword):
    assert plword(word) == pword


@pytest.fixture
def simple_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('this is a test\nof my translation program\n')
    return f


def test_simple(simple_file):
    assert(plfile(simple_file)
           ) == 'histay isway away esttay ofway ymay ranslationtay rogrampay'
