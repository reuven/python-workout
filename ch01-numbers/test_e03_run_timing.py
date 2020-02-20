from e03_run_timing import run_timing
from io import StringIO
import pytest


def test_no_input_generates_exception(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))

    with pytest.raises(ZeroDivisionError):
        run_timing()


def test_bad_input_generates_exception(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('abc\n\n'))

    with pytest.raises(ValueError):
        run_timing()


def test_one_run(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('1\n\n'))

    run_timing()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith("Average of 1.0, over 1 runs\n")


def test_10_runs(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(
        '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n\n'))

    run_timing()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith("Average of 5.5, over 10 runs\n")
