#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all method is design for init main process
import logging
import os
import traceback
import pickle

from config_helper import ConfigHelper
from global_info import GlobalInfo
from custom_libs.file_encoding import trim_file_bom
from utils.serialize_data import SerializeData


class InitHelper(object):

    @staticmethod
    def init_app_conf(app_root_path):
        """
            get config from config file and load some item to memory

        Returns:
            False: load failed
            True: load success
        """
        logger_main = logging.getLogger(GlobalInfo.logger_main)
        try:
            app_config_file_path = app_root_path + '/config/app_config.conf'
            # trim Bom
            trim_file_bom(app_config_file_path)
            ConfigHelper().init(app_config_file_path)

            return True
        except:
            logger_main.error('init app config failed')
            logger_main.error(traceback.format_exc())
            return False

    @staticmethod
    def init_app_path(app_root_path):
        """
            get config from config file and load some item to memory

        Returns:
            False: load failed
            True: load success
        """
        logger_main = logging.getLogger(GlobalInfo.logger_main)
        try:
            GlobalInfo.log_path = app_root_path + os.sep + 'log'

            # init path
            if os.path.exists(GlobalInfo.log_path) is False:
                os.makedirs(GlobalInfo.log_path)
            if os.path.exists(GlobalInfo.app_root_path) is False:
                os.makedirs(GlobalInfo.app_root_path)

            return True

        except:

            logger_main.error('init app path failed')
            logger_main.error(traceback.format_exc())
            return False

    @staticmethod
    def init_serialize_data(persistent_data_path):
        logger_main = logging.getLogger(GlobalInfo.logger_main)
        try:
            # init serialize data
            pd = open(persistent_data_path + 'persistent_data', 'r')
            SerializeData().init(pickle.load(pd))
            return True

        except:

            logger_main.info('persistent data path not exit')
            return False

    @staticmethod
    def init_frontend_conf(app_instance):
        logger_main = logging.getLogger(GlobalInfo.logger_main)
        try:
            # add global config for offline map
            front_conf = {}

            app_instance.add_template_global(front_conf, 'front_conf')
            return True

        except:

            logger_main.info('init offline map config filed')
            return False
