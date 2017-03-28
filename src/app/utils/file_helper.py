#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import os
import shutil
import traceback
from flask import logging
from utils.global_info import GlobalInfo


def remove_match_file(root_dir, match, del_mode=-1):
        """
        Args:
            root_dir:
            match:  math string to find which file should be deleted
            del_mode: del file model -1: del all not match file,0 del all match file

        Returns:

        """
        try:
            if os.path.exists(root_dir) is False:
                return False

            dirs = os.listdir(root_dir)
            for dir in dirs:
                if dir.find(match) == del_mode:
                    delete_path = root_dir + dir
                    if os.path.exists(delete_path):
                        if os.path.isfile(delete_path):
                            os.remove(delete_path)
                        else:
                            shutil.rmtree(delete_path)
            return True
        except:
            log = logging.getLogger(GlobalInfo.logger_main)
            log.debug("remove math file error!")
            log.error(traceback.format_exc())
            return False


def remove_old_file(root_dir, time):
        """
        Args:
            root_dir:
            time:  time division
            del_mode: del file model -1: del all not match file,0 del all match file

        Returns:

        """
        try:
            if os.path.exists(root_dir) is False:
                return False

            dirs = os.listdir(root_dir)
            if len(dirs) <= 1:
                return True
            for dir in dirs:
                if dir[:len(time)] < time and len(os.listdir(root_dir)) > 1:
                    delete_path = root_dir + dir
                    if os.path.exists(delete_path):
                        if os.path.isfile(delete_path):
                            os.remove(delete_path)
                        else:
                            shutil.rmtree(delete_path)
            return True
        except:
            log = logging.getLogger(GlobalInfo.logger_main)
            log.debug("remove math file error!")
            log.error(traceback.format_exc())
            return False