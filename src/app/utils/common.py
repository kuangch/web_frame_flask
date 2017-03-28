#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2015 Dilusense Inc. All Rights Reserved.

"""Some common classes"""

import threading
from datetime import datetime

from flask import logging

from utils.global_info import GlobalInfo


def fun_execute_time(func):
    """A decorator that can print execution microseconds of a function"""

    def _fun_execute_time(*args, **kwargs):
        begin_time = datetime.now()
        re = func(*args, **kwargs)
        end_time = datetime.now()
        sub_time = (end_time - begin_time)
        sub_ms = sub_time.seconds * 1000 + sub_time.microseconds / 1000
        if GlobalInfo.is_debug:
            logging.getLogger(GlobalInfo.logger_main)\
                .debug(func.func_name + ' execute time is:' + str(sub_ms) + ' ms')
        return re

    return _fun_execute_time


class FunctionThread(threading.Thread):
    """Through the thread to perform a function

    Example:
        FunctionThread(functionName,param1,param2)
    """

    def __init__(self, func, *args):
        """init thread
        Args:
            func:function name
            *args:parameters
        """

        self.func = func
        self.args = args
        threading.Thread.__init__(self)

    def run(self):
        if len(self.args) == 0:
            self.func()
        else:
            self.func(*self.args)

