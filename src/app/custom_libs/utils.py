#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# utils


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


def md5(str):
    """ calculate md5 value of a string
    Args:
        str: string which want to calculate md5 value

    Returns:
        md5 value
    """
    import hashlib
    import types
    if isinstance(str, types.StringType):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''
