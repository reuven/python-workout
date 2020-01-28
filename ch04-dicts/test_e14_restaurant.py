from e14_restaurant import restaurant
import pytest
from io import StringIO


def test_order_nothing(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('Your total is 0\n')


def test_order_one_entree(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('sandwich\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert captured_out.endswith('Your total is 10\n')


def test_order_two_entrees(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('sandwich\nsandwich\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert 'sandwich costs 10, total is 20' in captured_out
    assert captured_out.endswith('Your total is 20\n')


def test_order_many_items(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(
        'sandwich\nsandwich\nsalad\nelephant\ntea\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert 'sandwich costs 10, total is 20' in captured_out
    assert 'salad costs 9, total is 29' in captured_out
    assert 'We are fresh out of elephant today' in captured_out
    assert 'tea costs 7, total is 36' in captured_out
    assert captured_out.endswith('Your total is 36\n')
