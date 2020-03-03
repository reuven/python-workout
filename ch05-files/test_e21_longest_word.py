from e21_longest_word import find_longest_word, find_all_longest_words
import pytest
from io import StringIO


@pytest.fixture
def empty_file(tmp_path):
    f = tmp_path / 'emptyfile.txt'
    f.write_text('')
    return f


@pytest.fixture
def small_file(tmp_path):
    f = tmp_path / 'smallfile.txt'
    f.write_text('''This is the first line
and this is the second line''')
    return f


@pytest.fixture
def big_file(tmp_path):
    f = tmp_path / 'bigfile.txt'
    f.write_text('''This is the first line of a big file

and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


def test_small_file(small_file):
    assert find_longest_word(small_file) == 'second'


def test_big_file(big_file):
    assert find_longest_word(big_file) == 'encyclopedia'


def test_empty_directory(tmp_path):
    assert find_all_longest_words(tmp_path) == {}


def test_one_file(tmp_path, empty_file):
    assert find_all_longest_words(tmp_path) == {'emptyfile.txt': ''}


def test_all_files(tmp_path, empty_file, small_file, big_file):
    assert find_all_longest_words(tmp_path) == {'emptyfile.txt': '',
                                                'smallfile.txt': 'second',
                                                'bigfile.txt': 'encyclopedia'}
