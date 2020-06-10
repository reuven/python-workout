from e40_limited_size_bowl import Scoop, Bowl


def test_basic():
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('flavor 4')
    s5 = Scoop('flavor 5')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s4, s5)

    assert len(b.scoops) == 3
    assert s1 in b.scoops
    assert s2 in b.scoops
    assert s3 in b.scoops

    assert str(b) == 'chocolate\nvanilla\npersimmon'
