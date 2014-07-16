import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5566")
socket.setsockopt(zmq.SUBSCRIBE, "HELLO")

while True:
     message = socket.recv()
     print repr(message)