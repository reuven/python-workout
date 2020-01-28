from e15_rain import get_rainfall
import pytest
from io import StringIO


def test_nothing(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))
    get_rainfall()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip() == 'Enter city name:'


def test_one_city(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Tel Aviv\n5\n\n'))
    get_rainfall()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('Tel Aviv: 5\n')


def test_two_cities(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Tel Aviv\n5\nJerusalem\n3\n\n'))
    get_rainfall()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('Tel Aviv: 5\nJerusalem: 3\n')


def test_repeat_city(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(
        'Tel Aviv\n5\nJerusalem\n3\nTel Aviv\n7\n\n'))
    get_rainfall()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('Tel Aviv: 12\nJerusalem: 3\n')


def test_no_checking_of_rain_input(monkeypatch, capsys):
    with pytest.raises(ValueError):
        monkeypatch.setattr('sys.stdin', StringIO('Tel Aviv\nabc\n\n'))
        get_rainfall()
