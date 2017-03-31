#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# subscriber for camera frame data
import json

import threading
import traceback
import sys

import zmq

from flask import logging

from msg_trans import TransMsg, MsgTpye, SocketioHelper
from utils.global_info import GlobalInfo


class SubsMsgServer(threading.Thread):

    _logger = logging.getLogger(GlobalInfo.logger_main)
    run_flag = True

    def __init__(self, ip, port):

        context = zmq.Context()
        self._response = context.socket(zmq.SUB)
        self._ip = ip
        try:
            self._response.connect("tcp://"+ip+":" + port)
            self._response.setsockopt_string(zmq.SUBSCRIBE, ''.decode('utf-8'))
        except:
            exstr = traceback.format_exc()
            self._logger.error('zmq response connect error:  ' + exstr)
        threading.Thread.__init__(self)

    def run(self):
        while self.run_flag:
            msg = self._response.recv()
            msg_obj = TransMsg.GetRootAsTransMsg(msg, 0)
            msg_type = msg_obj.Type()

            if msg_type == MsgTpye.ZMQ_MSGTYPE_PERSON_PASS_INFO:
                self._logger.debug('recv person pass info msg: ' + msg_obj.Content())
                try:
                    msg = json.loads(msg_obj.Content())
                    msg['ip'] = self._ip
                    data = json.dumps({'ip': self._ip, 'data': msg})
                except:
                    data = ''

                SocketioHelper.send_msg2frontend(SocketioHelper.HEADER_PERSON_PASS_INFO, data)


if __name__ == '__main__':

    pass
