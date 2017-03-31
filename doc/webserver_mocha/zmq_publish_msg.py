# encoding: utf-8

import random
import string
import time
import datetime

from flask import json
import zmq

pool = ['a','b','c','d','e','f','g','h','i','j','A','B','C','D','E','F','G','H','I','J','K','M','1','2','3','4','5','6','7','8']

device_codes = ['B1M11SG07420', 'B1M11SG92690', 'B1M11SG30239', 'B1M11SG40179', 'B1M11SG29688',
                'B1M11SG92791', 'B1M11SG20461', 'B1M11SG18619', 'B1M11SG61951', 'B1M11SG59116']

from zmq_conn_port import ZMQPort
from zmq_flatbuf_msg_api import send_flatbuf_msg
from msg_type import MsgTpye


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:" + ZMQPort.SUBS_PERSON_PASS_INFO)

img = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUG \
BgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/2wBDAQICAgICAgUDAwUKBwYH \
CgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgr/wAAR \
CAB+AGYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAA \
AgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkK \
FhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWG \
h4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl \
5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREA \
AgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYk \
NOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOE \
hYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk \
5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9+KKKKACiiviD/gqb/wAFh/hh+xf4MvPh \
/wDCTWLDxF8SroNBBp0M2+LSDtBM1yV6YDArHnc2RjAyygm0j60+KPxz+DfwS0aTxD8XPifo \
fh2zi2+ZPq2oxwgZIA4Y5OSQBx1I9a+RfjZ/wX+/Ya+E3jk+DdG1nUPFFvGgM2teH40mtwTn \
5VyQWI49Bz1JyB+EPxh+NHxH+Ofi28+IfxS8bajrer3rlp7rULlpDgszBFB4RAWOEUBRngCu \
GLSZLEYBPT0qlEzc29j98NB/4ORf2HtR8Vx6JqOieLLTT2ZhJq0+lpiMAZBMaOzHPTAzyR2y \
R9b/ALP37bf7Lf7UNlb3PwS+MWk6zNcW6zCwSXZcxKQCA8bYZG5GVPIJwQDxX8pmpXTxg7D+ \
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 \
HcdTqOMbNd72PbjmmGa1uf/Z'


while True:

    person = {
        'serial_number': '42011619910620' + string.join(random.sample(pool, 4)).replace(" ", ""),
        'pass_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'id': '420116199106208017',
        'name': 'kch_' + str(random.randint(1, 9)),
        'gender': ['女', '男'][random.randint(0,1)],
        'nation': '武汉市',
        'address': '湖北省武汉市黄陂区北京街的卢村前端组',
        'id_image': img,
        'local_image': img,
        'device_id': device_codes[random.randint(0, 7)],
        'local_address': '北京市' + string.join(random.sample(pool, 4)).replace(" ", ""),
        '_1v1_result': random.randint(-1, 1),
        'blacklist_result': random.randint(-1, 1),
        'blacklist_handler': '黑名单报警处置意见'+ string.join(random.sample(pool, 4)).replace(" ", ""),
        'blacklist_message': '黑名单报警msg'+ string.join(random.sample(pool, 4)).replace(" ", ""),
        'blacklist_tag': '黑名单报警tag'+ string.join(random.sample(pool, 4)).replace(" ", ""),
        'blacklist_lib': '黑名单报警来源库'+ string.join(random.sample(pool, 4)).replace(" ", "")
    }

    time.sleep(1)
    # send_flatbuf_msg(socket, MsgTpye.ZMQ_MSGTYPE_INSTANT2DFRAME, f)
    send_flatbuf_msg(socket, MsgTpye.ZMQ_MSGTYPE_PERSON_PASS_INFO, json.dumps(person))
