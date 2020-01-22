from e01_guessing_game import guessing_game
from io import StringIO
import random


def test_correct(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith('Right!  The answer is 49\n')


def test_too_low_once(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('1\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 1 is too low!' in captured_out
    assert captured_out.endswith('Right!  The answer is 49\n')


def test_too_high_once(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('100\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 100 is too high!' in captured_out
    assert captured_out.endswith('Right!  The answer is 49\n')


def test_too_low_twice(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('1\n2\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 1 is too low!' in captured_out
    assert 'Your guess of 2 is too low!' in captured_out
    assert captured_out.endswith('Right!  The answer is 49\n')


def test_too_high_twice(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('100\n80\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 100 is too high!' in captured_out
    assert 'Your guess of 80 is too high!' in captured_out
    assert captured_out.endswith('Right!  The answer is 49\n')
