#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.


"""flask http server main program,local web server"""
from flask_socketio import SocketIO
from db.instance_db_connection import DBConnection
from msg_trans import SocketioHelper, ZMQPort
from msg_trans.thread_subs_msg import SubsMsgServer

from routes import *
from services.msg_center.portal_msg_manager import PortalMsgManager
from services.timer_task.timer_task_executor import execute_timer_tasks
from utils.global_info import GlobalInfo
from utils.init_helper import InitHelper


def setup():

    logger_main.info('setup server begin')

    # init app config
    InitHelper.init_app_conf(app.root_path)

    # init app path
    InitHelper.init_app_path(app.root_path)

    # init system config
    InitHelper.init_sys_conf()

    # add global config for frontend
    InitHelper.init_frontend_conf(app)

    # connect to database
    DBConnection().connect()

    # init socketIO
    SocketioHelper.set_socket(socketio)

    # thread that get pass person info
    PortalMsgManager.init_portals()

    logger_main.info('setup server end')

    # timer tasks
    # execute_timer_tasks()

    logger_main.info('server start success')


if __name__ == '__main__':

    logger_main = logging.getLogger(GlobalInfo.logger_main)
    logger_main.info('project work dir: ' + os.getcwd())
    global socketio
    socketio = SocketIO(app, async_mode='threading')
    setup()
    app_port = int(GlobalInfo.flask_port.strip())
    socketio.run(app=app, host='0.0.0.0', port=app_port)
