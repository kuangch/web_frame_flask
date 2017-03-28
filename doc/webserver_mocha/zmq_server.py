# encoding: utf8
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import zmq
import json

import time

from trans_msg import TransMsg
from zmq_flatbuf_msg_api import send_flatbuf_msg
from msg_type import MsgTpye
from zmq_conn_port import ZMQPort

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + ZMQPort.RQ)

cfg_data = {
    "auto_sleep_timeout": "30",
    "center_ip": "10.0.1.194",
    "collect_start_distance": "1.2",
    "dns_server": "114.114.114.114",
    "enable_handle": True,
    "is_auto_rotate": False,
    "is_loop_delete": False,
    "is_show_texture": False,
    "is_show_wireframe": False,
    "is_upload_by_gateway": False,
    "modeling_start_distance": "1.2",
    "modeling_timeout": "2",
    "mysql_db": "info_portal_local",
    "mysql_ip": "127.0.0.1",
    "mysql_name": "root",
    "mysql_pass": "12345",
    "mysql_port": "3306",
    "pass_mode": "0",
    "portal_address": "北京市",
    "portal_id": "DEVICE1",
    "portal_license": "ABC123",
    "portal_number": "",
    "portal_type": "0",
    "recognition_ip": "10.0.1.194",
    "strategy_time_begin": "16:00",
    "strategy_time_end": "23:00",
    "strategy_week": '{"mon":true,"tue":true,"wed":true}',
    "suppkg_ip": "10.0.1.159",
    "time_begin": "14:00",
    "time_end": "06:00",
    "upload_strategy": "2",
    "version": "v0.14-21",
    "week": "{}",
    "zmq_req_server": "tcp://*:5018",
    "is_custom_toggle": True,
    "valid_pass_threshold_count": "10",
    "is_play_alarm_sound": False
}

hardware_data = {
    'gate': True,
    'metal_detector': True,
    'identity_reader': False,
    'voice_box': True,
    'light': False,
    'phone_detector': True,
    'wifi_detector': True
}

while True:
    #  Wait for next request from client
    message = socket.recv()

    #  Do some 'work'
    msg_obj = TransMsg.GetRootAsTransMsg(message, 0)
    msg_type = msg_obj.Type()

    print('req type: %s' % msg_type)
    print('req para: %s' % msg_obj.Content())
    #  Send reply back to client

    if msg_type == MsgTpye.ZMQ_MSGTYPE_SETCFG:

        cfg_data = json.loads(msg_obj.Content())
        ret = {
            'code': 0,
            'msg': 'set config success'
        }
        send_flatbuf_msg(socket, msg_type, json.dumps(ret))
    if msg_type == MsgTpye.ZMQ_MSGTYPE_GETTAR:
        ret = {
            'code': 0,
            'msg': 'success',
            "data": {
                "tar_path": "/var/info_portal/test.txt"
            },
        }
        send_flatbuf_msg(socket, msg_type, json.dumps(ret))
    elif msg_type == MsgTpye.ZMQ_MSGTYPE_GETALLCFG:
        ret = {
            'code': 0,
            'msg': 'get config success',
            'data': cfg_data
        }
        send_flatbuf_msg(socket, msg_type, json.dumps(ret))
    elif msg_type == MsgTpye.ZMQ_MSGTYPE_HARDWARE_INFO:
        ret = {
            'code': 0,
            'msg': 'get config success',
            'data': hardware_data
        }
        send_flatbuf_msg(socket, msg_type, json.dumps(ret))
