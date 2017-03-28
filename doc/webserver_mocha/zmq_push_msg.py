import random
import zmq
import json
import time

from msg_trans import ZMQPort
from msg_type import MsgTpye
from trans_msg import *

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.PUSH)
print socket.connect("tcp://localhost:" + ZMQPort.PULL)


b = flatbuffers.Builder(0)
info = (1, 2, 3, 4)
msg_content = {
    'processing': 1
}
random.seed()

while True:
    if info is not None:

        msg_content['processing'] = info[random.randint(0, 3)]
        if(msg_content['processing']) == 2:
            msg_content = {
                'processing': 2,
                'serial_number': '123456'
            }
        msg = b.CreateString(json.dumps(msg_content))
    else:
        msg = b.CreateString('')

    TransMsgStart(b)
    TransMsgAddType(b, MsgTpye.ZMQ_MSGTYPE_PROCESS)
    TransMsgAddContent(b, msg)
    msT = TransMsgEnd(b)
    b.Finish(msT)

    h = b.Head()
    socket.send(b.Bytes[h:])

    time.sleep(2)
