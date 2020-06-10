from e37_menu import menu
from io import StringIO
import pytest


def funca():
    return 'I am funca'


def funcb():
    return 'I am funcb'


@pytest.mark.parametrize('choice,output', [
    ('a', 'I am funca'),
    ('b', 'I am funcb')
])
def test_choices(monkeypatch, capsys, choice, output):
    monkeypatch.setattr('sys.stdin', StringIO(f'{choice}\n'))
    output = menu(a=funca, b=funcb)
    captured_out, captured_err = capsys.readouterr()

    assert 'a/b' in captured_out
    assert output.endswith(output)


def test_bad_choice(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('c\na\n'))
    output = menu(a=funca, b=funcb)
    captured_out, captured_err = capsys.readouterr()

    assert 'a/b' in captured_out
    assert 'Not a valid option' in captured_out
    assert output.endswith('I am funca')
