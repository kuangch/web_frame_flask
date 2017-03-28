#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

"""Socketio helper class"""

import traceback


class SocketioHelper:

    _NAMESPACE = '/notification_push'

    HEADER_PERSON_PASS_INFO = "person_pass_info"

    _socket = None
    _logger = None

    @classmethod
    def set_socket(cls, socket):
        cls._socket = socket

    @classmethod
    def set_logger(cls, logger):
        cls._logger = logger

    @staticmethod
    def send_msg2frontend(msg_type, data):
        """
        send 2d best frame info msg to frontend
        Returns:

        """
        try:
            SocketioHelper._socket.emit(msg_type, {'data': data}, namespace=SocketioHelper._NAMESPACE)
        except:
            if SocketioHelper._logger is not None:
                exstr = traceback.format_exc()
                SocketioHelper._logger.error('send msg to frontend error: ' + exstr)


if __name__ == '__main__':
    pass
