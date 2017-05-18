#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all api is for frontend interface
import json
import logging
import traceback

from flask import request

from flask_application import app
from utils.global_info import GlobalInfo
from utils.my_constant import MyConstant
from utils.serialize_utils import SerializeUtils


front_conf = {}

@app.route('/config/getSettings')
def get_settings():

    try:
        cfg = SerializeUtils.get(MyConstant.sys_config_serialize_data_key)
        if cfg is None:
            cfg = {}
        return json.dumps({'code': 0, 'msg': 'get sys config success', 'data': cfg})
    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
        return json.dumps({'code': -1, 'msg': 'get sys config wrong!'})


@app.route('/config/postSettings', methods=['POST'])
def post_settings():

    try:
        old_cfg = SerializeUtils.get(MyConstant.sys_config_serialize_data_key)
        if old_cfg is None:
            old_cfg = {}

        param = request.form.get('sysconfig', '{}')

        try:
            new_cfg = json.loads(param)
        except:
            logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
            return json.dumps({'code': -1, 'msg': 'param error'})

        # merge config
        cfg = dict(old_cfg.items() + new_cfg.items())

        SerializeUtils.update(MyConstant.sys_config_serialize_data_key, cfg)
        return json.dumps({'code': 0, 'msg': 'sys config success'})

    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
        return json.dumps({'code': -1, 'msg': 'submit wrong!'})


