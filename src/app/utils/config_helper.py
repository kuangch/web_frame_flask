#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2015 Dilusense Inc. All Rights Reserved.

import ConfigParser
import logging
import traceback
import sys

from global_info import GlobalInfo


reload(sys)
sys.setdefaultencoding('utf8')


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class ConfigHelper(object):
    """This is a helper class for reading and writing configuration
    """
    __metaclass__ = Singleton

    __config = None
    __path = None
    __logger = None

    def init(self, __path):
        """init __config instance and init GlobalInfo
        Args:
            __path:__config file __path

        Return:
            None
        """
        if self.__config is not None and self.__logger is not None:
            self.__logger.debug('ConfigHelper instance has been inited')
            return True
        try:
            self.__logger = logging.getLogger(GlobalInfo.logger_main)
            self.__path = __path
            self.__config = ConfigParser.ConfigParser()
            with open(__path) as cfgfile:
                self.__config.readfp(cfgfile)
            self._init_global_info()
            self.__logger.info('ConfigHelper init success!')
            return True
        except:
            self.__logger.error('ConfigHelper init wrong!')
            self.__logger.error(traceback.format_exc())
            return False

    def _init_global_info(self):
        """Reading configuration information from a configuration file, and then assign values to the GlobalInfo"""

        dict = self.__config._sections
        keys_sections = dict.keys()
        for keys_section in keys_sections:
            keys = dict[keys_section].keys()
            for key in keys[1:]:
                if dict[keys_section][key] == 'true':
                    GlobalInfo.__dict__[key] = True
                    continue
                if dict[keys_section][key] == 'false':
                    GlobalInfo.__dict__[key] = False
                    continue
                GlobalInfo.__dict__[key] = dict[keys_section][key]

    def update_config_item(self, section, key, value):
        """Update __config item value
        Args:
            section:__config section
            key: key in this section
            value: value in this section

        Return:
            True or False
        """

        try:
            self.__config.set(section, key, value)
            with open(self.__path, 'w') as file:
                self.__config.write(file)
            GlobalInfo.__dict__[key] = value
            return True
        except:
            self.__logger.error(traceback.format_exc())
            return False

    def get_config_item(self, section, key):
        """Get __config item value
        Args:
            section:__config section
            key: key in this section
            value: value in this section

        Return:
            __config item value or None
        """
        try:
            return self.__config.get(section, key)
        except:
            self.__logger.error(traceback.format_exc())
            return None
