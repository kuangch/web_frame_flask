#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all api is for frontend interface
from flask import render_template
from flask_application import app


@app.route('/')
def index():
    return render_template('index.html')
