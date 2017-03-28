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


class SerializeData(object):
    __metaclass__ = Singleton

    __data = {}

    def __contains__(self, key):
        return key in self.__data

    def init(self, data):
        self.__data = data

    def data(self):
        return self.__data

    def update(self, key, value):
        self.__data[key] = value

    def get(self, key):
        if key in self.__data:
            return self.__data[key]
        else:
            return None
