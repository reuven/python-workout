from e39_bowl import Scoop, Bowl


def test_basic():
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)

    assert len(b.scoops) == 3
    assert s1 in b.scoops
    assert s2 in b.scoops
    assert s3 in b.scoops

    assert str(b) == 'chocolate\nvanilla\npersimmon'
