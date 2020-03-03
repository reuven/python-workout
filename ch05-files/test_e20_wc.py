from e20_wc import wordcount
import pytest
from io import StringIO


@pytest.fixture
def empty_file(tmp_path):
    f = tmp_path / 'textfile'
    f.write_text('')
    return f


@pytest.fixture
def simple_file(tmp_path):
    f = tmp_path / 'wcfile.txt'
    f.write_text('''This is a test file.

It contains 28 words and 20 different words.

It also contains 165 characters.

It also contains 11 lines.

It is also self-referential.

Wow!''')
    return f


def test_empty(empty_file, capsys):
    wordcount(empty_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """characters: 0
words: 0
lines: 0
unique words: 0
"""


def test_simple(simple_file, capsys):
    wordcount(simple_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """characters: 164
words: 28
lines: 11
unique words: 20
"""
