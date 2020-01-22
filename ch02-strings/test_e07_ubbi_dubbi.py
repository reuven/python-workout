from e07_ubbi_dubbi import ubbi_dubbi
from io import StringIO
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('papaya', 'pubapubayuba'),
    ('elephant', 'ubelubephubant'),
    ('testing', 'tubestubing'),
    ('banana', 'bubanubanuba'),
])
def test_simple(input_word, output_word, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(f'{input_word}\n'))
    ubbi_dubbi()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output_word}\n')
