#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# thread for pull message form work threading

import threading
import traceback
import json

import zmq
from flask import logging

from socketio_helper import SocketioHelper
from trans_msg import TransMsg
from msg_type import MsgTpye
from utils.global_info import GlobalInfo


class RecordMsgType():
    START = 1
    SUCCESS = 2
    FAILED = 3
    TIMEOUT = 4


class PullMsgServer(threading.Thread):

    _logger = logging.getLogger(GlobalInfo.logger_main)

    def __init__(self, port):

        context = zmq.Context()
        self._response = context.socket(zmq.PULL)
        try:
            self._response.bind('tcp://*:' + port)
        except:
            exstr = traceback.format_exc()
            self._logger.error('zmq response bind error:  ' + exstr)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg = self._response.recv()
            msg_obj = TransMsg.GetRootAsTransMsg(msg, 0)
            msg_type = msg_obj.Type()

            try:
                if msg_type == MsgTpye.ZMQ_MSGTYPE_PERSON_PASS_INFO:
                    msg_info = json.loads(msg_obj.Content())
                    SocketioHelper.send_msg2frontend(SocketioHelper.HEADER_PERSON_PASS_INFO, msg_info)

            except:
                self._logger.error(traceback.format_exc())


if __name__ == '__main__':

    pass
