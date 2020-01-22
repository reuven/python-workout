#!/usr/bin/env python3


def myxml(tagname, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f"<{tagname}{attrs}>{content}</{tagname}>"
