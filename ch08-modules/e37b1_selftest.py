#!/usr/bin/env python3

"""Solution to chapter 8, exercise 37, beyond 1: selftest"""

import subprocess
import sys
from io import StringIO


def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')


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


if __name__ == '__main__':
    program_name = sys.argv[0]

    subprocess.run(f'pytest -vv {program_name}', shell=True)
