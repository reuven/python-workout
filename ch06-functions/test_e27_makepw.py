from e27_makepw import create_password_generator
import random
import pytest
import string


@pytest.mark.parametrize('pool, size, pw', [
    ('abcdef', 8, 'ddaceddc'),
    ('!@#$%', 8, '$$!#%$$#'),
    (string.ascii_lowercase, 20, 'mynbiqpmzjplsgqejeyd')
])
def test_simple(pool, size, pw):
    random.seed(0)
    create_password = create_password_generator(pool)
    output = create_password(size)
    assert len(output) == size
    assert output == pw
