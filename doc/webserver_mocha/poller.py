#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# a single instance for zmq request

import zmq

from flask import json

from msg_trans import MsgTpye
from trans_msg import *
from zmq_conn_port import ZMQPort

from zmq_flatbuf_msg_api import send_flatbuf_msg


# default timeout for request
__DEFAULT_REQUEST_TIMEOUT = 1000 * 3
__POLL_INTERVAL = 300

#  Socket to talk to server
print "init RQ socket instance"
__socket = zmq.Context().socket(zmq.REQ)
__socket.connect("tcp://localhost:" + ZMQPort.RQ)

poller = zmq.Poller()
poller.register(__socket, zmq.POLLIN)

send_flatbuf_msg(__socket, MsgTpye.ZMQ_MSGTYPE_GETALLCFG, json.dumps({}))
reqs = 0
while reqs * __POLL_INTERVAL <= __DEFAULT_REQUEST_TIMEOUT:
    print('req')
    socks = dict(poller.poll(__POLL_INTERVAL))
    if __socket in socks and socks[__socket] == zmq.POLLIN:
        msg = __socket.recv()
        msgObj = TransMsg.GetRootAsTransMsg(msg, 0)
        print msgObj.Content()
    reqs = reqs + 1
