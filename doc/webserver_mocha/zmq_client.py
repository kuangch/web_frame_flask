import zmq

from doc.zmq_flatbuffer.TransMsg import *
import flatbuffers

context = zmq.Context()

"""
const int ZMQ_MSGTYPE_GETALLCFG = 0x1;
const int ZMQ_MSGTYPE_GETCFG    = 0x2;
const int ZMQ_MSGTYPE_SETCFG    = 0x3;
const int ZMQ_MSGTYPE_EXESQL    = 0x4;
const int ZMQ_MSGTYPE_PASSINFO  = 0x5;
"""

#  Socket to talk to server
print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
print socket.connect ("tcp://localhost:5555")


b = flatbuffers.Builder(0)
info = "insert into update_info(collector_id, update_time) values('webserver_mocha', now())"
if info is not None:
    msg = b.CreateString(info)
else:
    msg = b.CreateString('')


TransMsgStart(b)
TransMsgAddType(b, 4)
TransMsgAddContent(b, msg)
msT = TransMsgEnd(b)
b.Finish(msT)

h = b.Head()
socket.send(b.Bytes[h:])

msg = socket.recv()
msgObj = TransMsg.GetRootAsTransMsg(msg, 0)

print msgObj.Type()
print msgObj.Content()
