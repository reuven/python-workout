from e48_all_lines import all_lines
import pytest


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


def test_iterator(tmp_path):
    g = all_lines(tmp_path)
    assert iter(g) == g


def test_empty(tmp_path):
    lines = list(all_lines(tmp_path))
    assert len(lines) == 0


def test_simple(tmp_path, small_file, big_file):
    lines = list(all_lines(tmp_path))
    assert len(lines) == 9
    assert lines[0] == 'This is the first line\n'
    assert lines[-1] == 'but the biggest word will probably be encyclopedia'
