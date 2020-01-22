from e05_pig_latin import pig_latin
from io import StringIO
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('computer', 'omputercay'),
    ('table', 'abletay'),
    ('papaya', 'apayapay'),
    ('elephant', 'elephantway'),
    ('octopus', 'octopusway'),
    ('insightful', 'insightfulway')])
def test_simple(input_word, output_word, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(f'{input_word}\n'))
    pig_latin()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output_word}\n')
