import pytest
from e25_xml import myxml


def test_tagonly():
    assert myxml('tagname') == '<tagname></tagname>'


def test_tag_simple_text():
    assert myxml('tagname', 'text') == '<tagname>text</tagname>'


def test_nested():
    assert myxml('a',
                 myxml('b',
                       myxml('c', 'text'))) == '<a><b><c>text</c></b></a>'


def test_attributes():
    assert myxml('tagname',
                 a=1, b=2, c=3) == '<tagname a="1" b="2" c="3"></tagname>'


def test_attributes_and_text():
    assert myxml('tagname', 'text',
                 a=1, b=2, c=3) == '<tagname a="1" b="2" c="3">text</tagname>'
