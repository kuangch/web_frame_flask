#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

from fabric.api import *

env.hosts = ['10.0.1.50']
env.user = 'root'
env.password = '123'

repo_name = 'web_frame_flask'
project_name = 'web_frame_flask'
project_dst = '/opt/project/'

config_file_path = project_dst + project_name + '/config/app_config.conf'
config_file_tmp_path = project_dst + 'tmp/'


def deploy():

    with cd('/opt/repos/' + repo_name):
        run('git checkout master')
        run('git pull origin master')

        sudo('python build_release.py --src ./ --dst ' + project_dst)


def update():

    with cd('/opt/repos/' + repo_name):
        run('git checkout master')
        run('git pull origin master')

        sudo('mv ' + config_file_path + ' ' + config_file_tmp_path)
        sudo('python build_release.py --src ./ --dst ' + project_dst)
        sudo('mv ' + config_file_tmp_path + 'app_config.conf ' + config_file_path)
        restart()


def start():
    sudo('supervisorctl start ' + project_name)
    sudo('supervisorctl status')


def restart():
    sudo('supervisorctl restart ' + project_name)
    sudo('supervisorctl status')