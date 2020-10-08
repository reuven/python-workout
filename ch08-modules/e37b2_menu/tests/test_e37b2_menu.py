from e37b2_menu import menu, __version__

import sys
from io import StringIO


def test_version():
    assert __version__ == '0.1.0'


def test_good_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('a\n'))

    def a():
        return 'called a'

    returned_value = menu(a=a)

    assert 'called a' in returned_value


def test_bad_then_good_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('q\na\n'))

    def a():
        return 'called a'

    returned_value = menu(a=a)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert 'Not a valid option' in captured_stdout
    assert 'called a' in returned_value
