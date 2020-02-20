from e18_final_line import get_final_line
import pytest


@pytest.fixture
def empty_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('')
    return f


@pytest.fixture
def simple_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('abcd\nefgh\nijkl\n')
    return f


def test_empty(empty_file):
    assert get_final_line(empty_file) == ''


def test_simple(simple_file):
    assert get_final_line(simple_file) == 'ijkl\n'
