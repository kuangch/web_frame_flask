#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all method is design for init main process
import logging
import os
import traceback

from config_helper import ConfigHelper
from global_info import GlobalInfo
from custom_libs.file_encoding import trim_file_bom
from routes.config import front_conf
from utils.my_constant import MyConstant
from utils.serialize_data import SerializeData
from utils.serialize_utils import SerializeUtils


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

            GlobalInfo.persistent_data_path = os.path.dirname(os.path.abspath(app_root_path)) \
                                              + os.sep \
                                              + (GlobalInfo.local_data_dir_name or 'web_frame_flask_serialize_data') \
                                              + os.sep

            # init path
            if os.path.exists(GlobalInfo.log_path) is False:
                os.makedirs(GlobalInfo.log_path)
            if os.path.exists(GlobalInfo.persistent_data_path) is False:
                os.makedirs(GlobalInfo.persistent_data_path)


            return True

        except:

            logger_main.error('init app path failed')
            logger_main.error(traceback.format_exc())
            return False

    @staticmethod
    def init_sys_conf():
           logger_main = logging.getLogger(GlobalInfo.logger_main)
           try:
               SerializeData()\
                   .update(MyConstant.sys_config_serialize_data_key,
                           SerializeUtils.get(MyConstant.sys_config_serialize_data_key))
               return True
           except:
               logger_main.info('persistent data path not exit')
               return False

    @staticmethod
    def init_frontend_conf(app_instance):
        logger_main = logging.getLogger(GlobalInfo.logger_main)
        try:
            # add global config for offline map
            app_instance.add_template_global(front_conf, 'front_conf')
            return True

        except:

            logger_main.info('init front config filed')
            return False
