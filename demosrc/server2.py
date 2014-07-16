import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:6668")

while True:
    msg = socket.recv()
    print "Got", msg
    time.sleep(1)
    socket.send(msg)
