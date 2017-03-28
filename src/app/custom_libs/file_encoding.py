#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import codecs
import os


def trim_bom(str):
    if not str:
        return ''

    if len(str) < 3:
        return ''

    if str[:3] == codecs.BOM_UTF8:
        return str[3:]

    return str


def trim_file_bom(filename):
    if not filename:
        return False

    if not os.path.exists(filename):
        return False

    try:
        fp = open(filename, 'r')
        html_source = fp.read()
        fp.close()
    except:
        return False

    html_result = trim_bom(html_source)

    if html_result == html_source:
        return False

    try:
        fp = open(filename, 'w')
        fp.write(html_result)
        fp.close()
    except:
        return False
    return True
