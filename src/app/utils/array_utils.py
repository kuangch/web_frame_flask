#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
from flask import json


def merge_ids_string_arrays_to_array(res):
    """
    merge multi arrays to one array which contains all of per origin arrays
    :param res:
    :return:
    """
    ids_arr = []
    for item in res:
        ids = json.loads(item.ids)
        ids_arr = list(set(ids_arr).union(set(ids)))
    return ids_arr


def sum_ids_string_arrays_to_array(res):
    """
    sum multi arrays to one array which contains in all of arrays
    :param res:
    :return:
    """
    ids_arr = []
    for item in res:
        ids = json.loads(item.ids)
        ids_arr = ids_arr + ids
    return ids_arr
