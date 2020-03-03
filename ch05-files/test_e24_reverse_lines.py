from e24_reverse_lines import reverse_lines
import pytest


@pytest.fixture
def big_file(tmp_path):
    f = tmp_path / 'bigfile.txt'
    f.write_text('''This is the first line of a big file

and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


def test_reversing_lines(big_file):
    reverse_lines(big_file, 'output.txt')
    content = open('output.txt').read()
    assert len(content) == 167
    assert content[:18] == 'elif gib a fo enil'
    assert content[-18:] == 'w tseggib eht tub\n'
