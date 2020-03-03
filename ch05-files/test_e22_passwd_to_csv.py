from e22_passwd_to_csv import passwd_to_csv
import pytest


@pytest.fixture
def passwd_file(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('''
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
atara:x:1004:1005:Atara Lerner-Friedman,,,:/home/atara:/bin/bash
shikma:x:1005:1006:Shikma Lerner-Friedman,,,:/home/shikma:/bin/bash
amotz:x:1006:1007:Amotz Lerner-Friedman,,,:/home/amotz:/bin/bash
''')
    return f


def test_passwd_to_csv(passwd_file):
    passwd_to_csv(passwd_file, 'output.csv')

    csv_content = open('output.csv').read()
    assert len(csv_content) == 95
    assert csv_content.splitlines()[0] == 'root\t0'
    assert csv_content.splitlines()[-1] == 'amotz\t1006'
