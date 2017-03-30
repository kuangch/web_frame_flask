#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import re


class Regular(object):

    @staticmethod
    def verify_ip(ip_str):
        p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$"
                       "|^localhost$")
        if p.match(ip_str) is None:
            return False
        return True


