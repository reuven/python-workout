#!/usr/bin/env python3

"""Solution to chapter 6, exercise 25: myxml"""


def myxml(tagname, content='', **kwargs):
    """Takes a tag name (string), an optional content string,
and optional kwargs.

Returns a string in which "tagname" is an XML tag at the start and end,
"content" is placed in the middle of the tags, and
the key-value pairs of kwargs are inserted as attributes in the opening tag.
"""
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'
