#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# make a instance of flask
import logging
import logging.config
import os
import sys
from functools import wraps

from flask import Flask, make_response

from utils.log_helper import set_log_level_by_config_file

# change work dir
work_dir = os.path.abspath(sys.argv[0])
print('flask work dir change before: ' + work_dir)
if os.path.isfile(work_dir):
    work_dir = os.path.dirname(work_dir)
print('flask work dir change after: ' + work_dir)
os.chdir(work_dir)

app = Flask(__name__)

# config flask object parameters
app.root_path = "./"
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Solve the problem of jinja and angularjs conflict of separators
app.jinja_env.variable_start_string = "${"
app.jinja_env.variable_end_string = "}"

# init logger config
logging.config.fileConfig(app.root_path + '/config/logging.conf')

# set log level by config file
set_log_level_by_config_file(app.root_path + '/config/app_config.conf')


# deal with cross-domain request problem
def allow_cross_domain(func):
    """In order to deal with cross-domain request problem"""

    @wraps(func)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(func(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
        allow_headers = 'Referer,Accept,Origin,User-Agent'
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun
