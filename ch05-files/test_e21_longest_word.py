from e21_longest_word import find_longest_word, find_all_longest_words
import pytest
from io import StringIO


@pytest.fixture
def small_file(tmp_path):
    f = tmp_path / 'smallfile.txt'
    f.write_text('''This is the first line
and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


@pytest.fixture
def big_file(tmp_path):
    f = tmp_path / 'bigfile.txt'
    f.write_text('''This is the first line of a big file

and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


def test_empty(empty_file, capsys):
    wc(empty_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """characters: 0
words: 0
lines: 0
unique words: 0
"""


def test_simple(simple_file, capsys):
    wc(simple_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """characters: 164
words: 28
lines: 11
unique words: 20
"""
