#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import datetime

from flask import logging
from utils.file_helper import remove_old_file

from utils.global_info import GlobalInfo


__logger = logging.getLogger(GlobalInfo.logger_main)


# clear person info of pic, frame, model data task
def tt_1():

    time_division = datetime.datetime.now().strftime('%Y%m%d')
    pass


# clear real time pic data task
def tt_1():

    time_division = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime('%Y%m%d%H%M')
    pass
