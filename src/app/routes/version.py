#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all api is for frontend interface
import traceback

from flask_application import app, logging
from utils.global_info import GlobalInfo
from version_info import VERSION_INFO


@app.route('/v')
def v():

    vi_keys = [
        'version',
        'build_time'
    ]
    version_info = {}

    for key in vi_keys:
        version_info[key] = '未知'

    try:
        vi = VERSION_INFO

        if vi is not None:
            vi_arr = vi.split('@')

            for i in range(min(len(vi_arr), len(vi_keys))):
                version_info[vi_keys[i]] = vi_arr[i]
    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())

    return '软件版本: ' + version_info['version'] + '</br>' + '构建时间: ' + version_info['build_time']