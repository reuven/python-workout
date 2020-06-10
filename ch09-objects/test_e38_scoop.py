from e38_scoop import Scoop, create_scoops


def test_scoop():
    s = Scoop('a_flavor')
    assert s.flavor == 'a_flavor'
    s.flavor = 'abcd'
    assert s.flavor == 'abcd'


def test_create_scoops(capsys):
    create_scoops()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'chocolate\nvanilla\npersimmon\n'
