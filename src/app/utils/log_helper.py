#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

import ConfigParser
import logging
import logging.config
import traceback

from utils.global_info import GlobalInfo


def set_log_level_by_config_file(file_path):
    # init logger config
    logger_main = logging.getLogger(GlobalInfo.logger_main)

    # set log level
    try:
        config_parser = ConfigParser.ConfigParser()
        with open(file_path) as cfgfile:
            config_parser.readfp(cfgfile)
        level = config_parser.get('logger', 'logger_level')
        if level == 'DEBUG':
            logger_main.setLevel(logging.DEBUG)
        elif level == 'WARN':
            logger_main.setLevel(logging.WARN)
        else:
            logger_main.setLevel(logging.INFO)
    except:
        logger_main.setLevel(logging.INFO)
        logger_main.error(traceback.format_exc())

    logger_main.info('set logger lever to %s success' % logging.getLevelName(logger_main.level))
