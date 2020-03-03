from e23_test_scores import print_scores
import pytest


@pytest.fixture
def score_file_1(tmp_path):
    j1 = tmp_path / '9a.json'
    j1.write_text('''
[{"math" : 90, "literature" : 98, "science" : 97},
 {"math" : 65, "literature" : 79, "science" : 85},
 {"math" : 78, "literature" : 83, "science" : 75},
 {"math" : 92, "literature" : 78, "science" : 85},
 {"math" : 100, "literature" : 80, "science" : 90}
]
''')
    return j1


@pytest.fixture
def score_file_2(tmp_path):
    j2 = tmp_path / '9b.json'
    j2.write_text('''
[{"math" : 70, "literature" : 98, "science" : 97},
 {"math" : 65, "literature" : 83, "science" : 70},
 {"math" : 58, "literature" : 83, "science" : 75},
 {"math" : 72, "literature" : 78, "science" : 85},
 {"math" : 100, "literature" : 80, "science" : 90}
]
''')
    return j2


def test_scores(tmp_path, score_file_1, score_file_2, capsys):
    print_scores(tmp_path)
    captured_out, captured_err = capsys.readouterr()
    assert '9a.json' in captured_out
    assert '9b.json' in captured_out
    # assert captured_out.count(' min ') == 6
    # assert captured_out.count(' max ') == 6
    # assert captured_out.count(' average ') == 6
