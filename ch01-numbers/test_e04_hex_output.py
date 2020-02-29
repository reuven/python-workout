from e04_hex_output import hex_output
from io import StringIO
import pytest


def test_no_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))
    hex_output()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('0\n')


def test_bad_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('q\n'))
    with pytest.raises(ValueError):
        hex_output()


@pytest.mark.parametrize('user_input, output', [
    ('123', '291'),
    ('ff', '255'),
    ('abc123', '11256099')
])
def test_good_input(user_input, output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(user_input + '\n'))
    hex_output()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output}\n')
