from e41_bigbowl import Scoop, Bowl, BigBowl


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


def test_big():
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('flavor 4')
    s5 = Scoop('flavor 5')

    b = BigBowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s4, s5)

    assert len(b.scoops) == 5
    assert s1 in b.scoops
    assert s2 in b.scoops
    assert s3 in b.scoops
    assert s4 in b.scoops
    assert s5 in b.scoops

    assert str(b) == 'chocolate\nvanilla\npersimmon\nflavor 4\nflavor 5'
