#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class ZMQConns(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.cache = {}

    def __contains__(self, key):
        return key in self.cache

    def len(self):
        self.cache.__len__()

    def put(self, key, value):
        self.cache[key] = value

    def remove(self, key):
        if key in self.cache:
            self.cache.pop(key)

    def get_all(self):
        return self.cache

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None
