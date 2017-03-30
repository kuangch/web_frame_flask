#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import os
import pickle
import traceback
from flask import logging
from utils.global_info import GlobalInfo
from utils.serialize_data import SerializeData


class SerializeUtils(object):

    @staticmethod
    def update(key, data):

        SerializeData().update(key, data)
        if os.path.exists(GlobalInfo.persistent_data_path) is not True:
            os.mkdir(GlobalInfo.persistent_data_path)
        pd = open(GlobalInfo.persistent_data_path + key, 'w')
        pickle.dump(SerializeData().data(), pd)

    @staticmethod
    def get(key):
        pd = None
        try:
            try:
                pd = open(GlobalInfo.persistent_data_path + key, 'r')
                table = pickle.load(pd)
                return table[key]
            except:
                logging.getLogger(GlobalInfo.logger_main).info(GlobalInfo.persistent_data_path + key + ' is not exit')
                return None
        except:
            logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
            return None