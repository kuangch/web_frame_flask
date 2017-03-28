#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

"""This is a helper about database operations"""

import logging
import sys
import traceback

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import *
from utils.global_info import GlobalInfo

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


class DBConnection(object):
    """This is a helper class to access data in a mysql database by SQLAlchemy
    the single instance of db helper
    """
    __metaclass__ = Singleton

    __logger = None

    def connect(self):
        """Initialize the database, create a table

        Return:
            Ture or False
        """

        self.__logger = logging.getLogger(GlobalInfo.logger_main)

        if GlobalInfo.db_if_echo:
            db_if_echo = True
        else:
            db_if_echo = False

        try:
            database = 'mysql://' \
                       + GlobalInfo.db_user + ':' \
                       + GlobalInfo.db_pwd + '@' \
                       + GlobalInfo.db_address + ':' \
                       + GlobalInfo.db_port + '/' \
                       + GlobalInfo.db_name_info_portal + '?charset=' \
                       + GlobalInfo.db_charset

            self.__logger.debug('connect to db : %s', database)
            engine = create_engine(database,
                                   echo=db_if_echo,
                                   poolclass=sqlalchemy.pool.QueuePool,
                                   pool_size=100,
                                   pool_recycle=7200)
            if engine is not None:
                db_session = sessionmaker(bind=engine)
                __session = db_session()
                self.__logger.debug('connect db success!')
                return __session
            else:
                self.__logger.warn('connect db failed!')
                return None
        except Exception:
            self.__logger.error(traceback.format_exc())
            return None