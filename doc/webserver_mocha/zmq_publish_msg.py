# encoding: utf-8

import random
import time

from flask import json
import zmq

from zmq_conn_port import ZMQPort
from zmq_flatbuf_msg_api import send_flatbuf_msg
from msg_type import MsgTpye


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:" + ZMQPort.SUBS_PERSON_PASS_INFO)

person = {
    "name": "kch",
    "sex": "man"
}
while True:

    person['name'] = 'kch' + str(random.randint(1, 10))

    time.sleep(1)
    # send_flatbuf_msg(socket, MsgTpye.ZMQ_MSGTYPE_INSTANT2DFRAME, f)
    send_flatbuf_msg(socket, MsgTpye.ZMQ_MSGTYPE_PERSON_PASS_INFO, json.dumps(person))
