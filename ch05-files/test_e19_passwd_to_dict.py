from e19_passwd_to_dict import passwd_to_dict
import pytest
from io import StringIO


@pytest.fixture
def empty_passwd(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('')
    return f


@pytest.fixture
def simple_passwd(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('''root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
''')
    return f


@pytest.fixture
def complex_passwd(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('''root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
# this is a comment line
# and then we have some blank lines

sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
''')
    return f


def test_empty(empty_passwd):
    assert passwd_to_dict(empty_passwd) == {}


def test_simple(simple_passwd):
    d = passwd_to_dict(simple_passwd)
    assert len(d) == 9
    assert d['root'] == 0
    assert d['sys'] == 3
    assert d['mail'] == 8


def test_complex(complex_passwd):
    d = passwd_to_dict(complex_passwd)
    assert len(d) == 9
    assert d['root'] == 0
    assert d['sys'] == 3
    assert d['mail'] == 8
